// HH — lyric overlay for After Effects (File > Scripts > Run Script File...)
// Builds one comp with a transparent background: a 5 s title card, then each lyric line for 3 s,
// white Arabic text with the مدّ look (long kashida stretches drawn with the tatweel character ـ),
// revealed word by word in reading order out of a soft blur, a slow push while it holds,
// and a dissolve upward at the end of each line, like dust carried off in the backlight.
// Keep this file saved as UTF-8 (with BOM) so the Arabic text reads correctly.

(function HH_Lyrics() {

    // ================================ SETTINGS ================================

    // Fonts to try, in order: the first one installed is used. Family, full or PostScript name.
    // The مدّ works with any Arabic font; a light Naskh matches the references best.
    var FONTS = ["Sakkal Majalla", "Adobe Arabic", "Noto Naskh Arabic", "Geeza Pro", "Arial"];

    var COMP_NAME = "HH_Lyrics";
    var WIDTH = 2206;                // the takes' frame size (21:9); for the upscaled final use e.g. 3840 x 1646:
    var HEIGHT = 946;                // sizes and positions below are fractions, so everything scales with it
    var FPS = 24;

    var INTRO_DUR = 5;               // title card, seconds
    var PHRASE_DUR = 3;              // each lyric line, seconds

    // A single ـ marks where a word is stretched; the script turns each one into a long مدّ.
    // Move, add or remove ـ marks freely. Text without a mark is never stretched.
    var INTRO_TITLE = "هامـة المجـد";
    var INTRO_CREDIT = "كلمات الشيخ محمد بن راشد آل مكتوم";

    var LYRICS = [
        "يـا هامـة المجـد",
        "شـوق مسرّجـات الأمهـار",
        "خـزاين العِـز",
        "فـي كفّـك مفاتيحهـا",
        "ومـن يعسـف الخيـل",
        "ذات العـز والانتصـار",
        "إللـي تسابـق علـى مضمارهـا ريحهـا",
        "يقـدر يعسـف الظـروف الكايـده باقتـدار",
        "وترجـح لـه الكفـة إلـى رام ترجيحهـا",
        "مـن قوباسـك مـا يعـرف عزمـك الانهيـار",
        "ومـا كـل كـفٍ يهـز القلـب تلويحهـا",
        "نظـرة عيونـك تـدل الـدرب وأهـل القـرار",
        "علـى خطـى فكرتـك تضـوي مصابيحهـا"
    ];

    // مدّ (kashida stretch)
    var STRETCH = 5.0;               // length of each stretch, in font sizes (the references run about 5-7)
    var STRETCH_MIN = 1.5;           // long lines shorten their stretches to fit, but never below this
    var MADD_GROW = false;           // true: the stretches draw out while the line appears. They grow one
                                     // tatweel at a time, so the growth is stepped rather than smooth.
    var GROW_DUR = 0.8;              // seconds, when MADD_GROW is on

    // Layout, as fractions of the comp size
    var INTRO_CENTER = [0.70, 0.40]; // title card in shot 02's title space (right half, upper part)
    var INTRO_MAX_WIDTH = 0.52;      // of comp width
    var TITLE_SIZE = 0.115;          // of comp height
    var CREDIT_SIZE = 0.040;
    var CREDIT_GAP = 0.030;          // between title and credit, of comp height
    var LYRIC_CENTER = [0.50, 0.82]; // lyrics centred in the lower part of the frame
    var LYRIC_SIZE = 0.060;
    var LYRIC_MAX_WIDTH = 0.86;      // of comp width

    // Look
    var TEXT_COLOR = [1, 1, 1];
    var GLINT_COLOR = [1.0, 0.85, 0.62];  // warm gold, the film's backlight, passing once through the title
    var SHADOW = true;               // soft dark halo kept in the alpha, for legibility over bright dust
    var SHADOW_OPACITY = 35;         // percent
    var SHADOW_SOFTNESS = 0.030;     // of comp height

    // Motion
    var IN_DUR = 0.9;                // word-by-word reveal, seconds
    var OUT_DUR = 0.6;               // dissolve at the end of each line, seconds
    var IN_BLUR = 0.025;             // of comp height
    var OUT_BLUR = 0.020;
    var IN_RISE = 0.018;             // words rise into place from this far below, of comp height
    var OUT_RISE = 0.012;            // and drift up this far as they dissolve
    var PUSH = 2.0;                  // percent of slow scale-up over each line (the film's slow push)
    var REVEAL_REVERSED = false;     // set true if the words appear left to right instead of right to left

    var ADD_TO_RENDER_QUEUE = true;  // queued with an alpha output module; press Render when ready

    // ================================ HELPERS =================================

    var TATWEEL = "\u0640";

    // PostScript names to try when this After Effects has no font list (before version 24)
    var KNOWN_PS = {
        "Sakkal Majalla": "SakkalMajalla",
        "Adobe Arabic": "AdobeArabic-Regular",
        "Noto Naskh Arabic": "NotoNaskhArabic-Regular",
        "Geeza Pro": "GeezaPro",
        "Arial": "ArialMT"
    };

    function px(f) { return f * HEIGHT; }

    function lower(s) { return String(s).toLowerCase(); }

    function repeat(s, n) { var out = ""; for (var i = 0; i < n; i++) out += s; return out; }

    function fontField(f, key) {
        try { return f[key] ? String(f[key]) : ""; } catch (e) { return ""; }
    }

    function isRegular(f) {
        var s = lower(fontField(f, "styleName"));
        return s === "regular" || s === "normal" || s === "book" || s === "medium";
    }

    // Font list through app.fonts (After Effects 24.0 and later). Returns false when unavailable.
    function eachFont(callback) {
        var groups;
        try { groups = app.fonts.allFonts; } catch (e) { return false; }
        if (!groups) return false;
        for (var i = 0; i < groups.length; i++) {
            var g = groups[i];
            if (g && g.length !== undefined && typeof g !== "string") {
                for (var j = 0; j < g.length; j++) callback(g[j]);
            } else {
                callback(g);
            }
        }
        return true;
    }

    function findFont(name) {
        var key = lower(name), exact = null, partial = null;
        var fields = ["postScriptName", "fullName", "nativeFullName", "familyName", "nativeFamilyName"];
        var listed = eachFont(function (f) {
            for (var k = 0; k < fields.length; k++) {
                var v = lower(fontField(f, fields[k]));
                if (!v) continue;
                if (v === key) { if (!exact || isRegular(f)) exact = f; }
                else if (!partial && v.indexOf(key) >= 0) partial = f;
            }
        });
        return { listed: listed, font: exact || partial };
    }

    // Without a font list: set the PostScript name on a test layer and keep it if it sticks.
    function fontSticks(comp, ps) {
        var layer = comp.layers.addText("test");
        var prop = layer.property("ADBE Text Properties").property("ADBE Text Document");
        var ok = false;
        try {
            var td = prop.value;
            td.font = ps;
            prop.setValue(td);
            ok = prop.value.font === ps;
        } catch (e) {}
        layer.remove();
        return ok;
    }

    function chooseFont(comp) {
        for (var i = 0; i < FONTS.length; i++) {
            var r = findFont(FONTS[i]);
            if (r.font) return { ps: fontField(r.font, "postScriptName"), label: FONTS[i] };
            if (!r.listed) {
                var ps = KNOWN_PS[FONTS[i]] || FONTS[i];
                if (fontSticks(comp, ps)) return { ps: ps, label: FONTS[i] };
            }
        }
        return null;
    }

    function tr(layer, matchName) { return layer.property("ADBE Transform Group").property(matchName); }

    function easeKeys(prop) {
        var dims = 1;
        if (prop.propertyValueType === PropertyValueType.TwoD) dims = 2;
        else if (prop.propertyValueType === PropertyValueType.ThreeD) dims = 3;
        var ease = [];
        for (var d = 0; d < dims; d++) ease.push(new KeyframeEase(0, 70));
        for (var k = 1; k <= prop.numKeys; k++) prop.setTemporalEaseAtKey(k, ease, ease);
    }

    function textProp(layer) { return layer.property("ADBE Text Properties").property("ADBE Text Document"); }

    function makeText(comp, str, sizePx, name, fontPS) {
        var layer = comp.layers.addText(str);
        layer.name = name;
        var prop = textProp(layer);
        var td = prop.value;
        try { td.resetCharStyle(); } catch (e1) {}
        try { td.resetParagraphStyle(); } catch (e2) {}
        td.text = str;
        td.fontSize = sizePx;
        td.applyFill = true;
        td.fillColor = TEXT_COLOR;
        td.applyStroke = false;
        td.tracking = 0;                                 // tracking would break the Arabic joins
        if (fontPS) { try { td.font = fontPS; } catch (e0) {} }
        td.justification = ParagraphJustification.CENTER_JUSTIFY;
        try { td.direction = ParagraphDirection.DIRECTION_RIGHT_TO_LEFT; } catch (e3) {}
        try { td.composerEngine = ComposerEngine.UNIVERSAL_TYPE_ENGINE; } catch (e4) {}
        prop.setValue(td);
        return layer;
    }

    function setText(layer, str) {
        var prop = textProp(layer);
        var td = prop.value;
        td.text = str;
        prop.setValue(td);
    }

    function rectOf(layer) { return layer.sourceRectAtTime(layer.inPoint, false); }

    // Scale the font size down if the line is wider than maxWidthPx.
    function fitWidth(layer, maxWidthPx) {
        var r = rectOf(layer);
        if (r.width <= maxWidthPx) return;
        var prop = textProp(layer);
        var td = prop.value;
        td.fontSize = td.fontSize * (maxWidthPx / r.width);
        prop.setValue(td);
    }

    // Width of one tatweel per pixel of font size, measured in the chosen font.
    function measureTatweel(comp, fontPS) {
        var layer = makeText(comp, repeat(TATWEEL, 40), 100, "measure", fontPS);
        var w = layer.sourceRectAtTime(0, false).width / 40 / 100;
        layer.remove();
        return w;
    }

    // Lay out a line with مدّ stretches at its ـ marks: as long as STRETCH allows, shorter if the line
    // would be wider than maxWidthPx, never shorter than STRETCH_MIN; the font shrinks only after that.
    // Returns the layer; the number of tatweels per stretch is kept in layer.comment.
    function makeMadd(comp, marked, sizePx, name, fontPS, maxWidthPx, tatweelPerPx) {
        var parts = String(marked).replace(/\u0640+/g, TATWEEL).split(TATWEEL);
        var stretches = parts.length - 1;
        var layer = makeText(comp, parts.join(""), sizePx, name, fontPS);
        var n = 0;
        if (stretches > 0 && tatweelPerPx > 0) {
            var tw = tatweelPerPx * sizePx;
            var bare = rectOf(layer).width;
            n = Math.round(STRETCH * sizePx / tw);
            var fits = Math.floor((maxWidthPx - bare) / (stretches * tw));
            if (fits < n) n = fits;
            var least = Math.ceil(STRETCH_MIN * sizePx / tw);
            if (n < least) n = least;
            setText(layer, parts.join(repeat(TATWEEL, n)));
        }
        fitWidth(layer, maxWidthPx);
        layer.comment = "madd " + n;
        if (MADD_GROW && n > 0) {
            textProp(layer).expression =
                "var b = \"" + parts.join("\\u0640") + "\";\n" +
                "var n = Math.round(easeOut(time, inPoint, inPoint + " + GROW_DUR + ", 0, " + n + "));\n" +
                "var s = \"\"; for (var i = 0; i < n; i++) s += \"\\u0640\";\n" +
                "b.split(\"\\u0640\").join(s);";
        }
        return layer;
    }

    // Anchor at the centre of the text, layer at pos. Returns the text's height.
    function centreAt(layer, pos) {
        var r = rectOf(layer);
        tr(layer, "ADBE Anchor Point").setValue([r.left + r.width / 2, r.top + r.height / 2]);
        tr(layer, "ADBE Position").setValue(pos);
        return r.height;
    }

    // Word-by-word reveal in reading order: opacity, blur and a small rise, on a range selector.
    function addReveal(layer, t0, dur) {
        var animators = layer.property("ADBE Text Properties").property("ADBE Text Animators");
        animators.addProperty("ADBE Text Animator");
        var anim = animators.property(animators.numProperties);
        anim.name = "Reveal";
        anim.property("ADBE Text Animator Properties").addProperty("ADBE Text Opacity");
        anim.property("ADBE Text Animator Properties").addProperty("ADBE Text Blur");
        anim.property("ADBE Text Animator Properties").addProperty("ADBE Text Position 3D");
        anim.property("ADBE Text Selectors").addProperty("ADBE Text Selector");
        anim = animators.property(animators.numProperties);    // fresh reference after adding properties
        var props = anim.property("ADBE Text Animator Properties");
        props.property("ADBE Text Opacity").setValue(0);
        props.property("ADBE Text Blur").setValue([px(IN_BLUR), px(IN_BLUR)]);
        props.property("ADBE Text Position 3D").setValue([0, px(IN_RISE), 0]);
        var sel = anim.property("ADBE Text Selectors").property(1);
        var adv = sel.property("ADBE Text Range Advanced");
        adv.property("ADBE Text Range Type2").setValue(3);               // based on words
        adv.property("ADBE Text Selector Smoothness").setValue(100);
        var p;
        if (REVEAL_REVERSED) {
            p = sel.property("ADBE Text Percent End");
            p.setValueAtTime(t0, 100);
            p.setValueAtTime(t0 + dur, 0);
        } else {
            p = sel.property("ADBE Text Percent Start");
            p.setValueAtTime(t0, 0);
            p.setValueAtTime(t0 + dur, 100);
        }
        easeKeys(p);
    }

    // A warm band of colour that travels once through the text in reading order.
    function addGlint(layer, t0, dur) {
        var animators = layer.property("ADBE Text Properties").property("ADBE Text Animators");
        animators.addProperty("ADBE Text Animator");
        var anim = animators.property(animators.numProperties);
        anim.name = "Glint";
        anim.property("ADBE Text Animator Properties").addProperty("ADBE Text Fill Color");
        anim.property("ADBE Text Selectors").addProperty("ADBE Text Selector");
        anim = animators.property(animators.numProperties);
        var fill = anim.property("ADBE Text Animator Properties").property("ADBE Text Fill Color");
        try { fill.setValue([GLINT_COLOR[0], GLINT_COLOR[1], GLINT_COLOR[2], 1]); }
        catch (e) { fill.setValue(GLINT_COLOR); }
        var sel = anim.property("ADBE Text Selectors").property(1);
        var adv = sel.property("ADBE Text Range Advanced");
        adv.property("ADBE Text Range Type2").setValue(1);   // characters: colour leaves the Arabic joins intact
        adv.property("ADBE Text Range Shape").setValue(5);   // round: a soft-edged band
        sel.property("ADBE Text Percent Start").setValue(0);
        sel.property("ADBE Text Percent End").setValue(30);
        var off = sel.property("ADBE Text Percent Offset");
        off.setValueAtTime(t0, REVEAL_REVERSED ? 100 : -30);
        off.setValueAtTime(t0 + dur, REVEAL_REVERSED ? -30 : 100);
        easeKeys(off);
    }

    // Slow push while the line holds, then the dissolve: opacity out, blur up, drift upward.
    function addHoldAndOut(layer, pos, t0, t1, startScale) {
        var scale = tr(layer, "ADBE Scale");
        scale.setValueAtTime(t0, [startScale, startScale, 100]);
        scale.setValueAtTime(t1, [100 + PUSH, 100 + PUSH, 100]);

        var opacity = tr(layer, "ADBE Opacity");
        opacity.setValueAtTime(t1 - OUT_DUR, 100);
        opacity.setValueAtTime(t1, 0);
        easeKeys(opacity);

        var position = tr(layer, "ADBE Position");
        position.setValueAtTime(t1 - OUT_DUR, pos);
        position.setValueAtTime(t1, [pos[0], pos[1] - px(OUT_RISE)]);
        easeKeys(position);

        var effects = layer.property("ADBE Effect Parade");
        effects.addProperty("ADBE Gaussian Blur 2");
        var blur = effects.property(effects.numProperties).property("ADBE Gaussian Blur 2-0001");
        blur.setValueAtTime(t1 - OUT_DUR, 0);
        blur.setValueAtTime(t1, px(OUT_BLUR));
        easeKeys(blur);

        if (SHADOW) {
            effects.addProperty("ADBE Drop Shadow");
            var ds = effects.property(effects.numProperties);
            try { ds.property("ADBE Drop Shadow-0001").setValue([0, 0, 0, 1]); }
            catch (e1) { ds.property("ADBE Drop Shadow-0001").setValue([0, 0, 0]); }
            var op = ds.property("ADBE Drop Shadow-0002");
            op.setValue(op.hasMax && op.maxValue > 100 ? SHADOW_OPACITY * 2.55 : SHADOW_OPACITY);
            ds.property("ADBE Drop Shadow-0004").setValue(0);             // distance: a halo, not an offset
            ds.property("ADBE Drop Shadow-0005").setValue(px(SHADOW_SOFTNESS));
        }
    }

    function addMarker(comp, t, text) {
        try { comp.markerProperty.setValueAtTime(t, new MarkerValue(text)); } catch (e) {}
    }

    function plain(marked) { return String(marked).replace(/\u0640+/g, ""); }

    // ================================= BUILD ==================================

    if (!app.project) app.newProject();
    app.beginUndoGroup("HH lyrics");

    var total = INTRO_DUR + LYRICS.length * PHRASE_DUR;
    var folder = app.project.items.addFolder(COMP_NAME);
    var comp = app.project.items.addComp(COMP_NAME, WIDTH, HEIGHT, 1, total, FPS);
    comp.parentFolder = folder;
    comp.bgColor = [0, 0, 0];

    var chosen = chooseFont(comp);
    var fontPS = chosen ? chosen.ps : null;                  // null: After Effects' default font
    var tatweelPerPx = measureTatweel(comp, fontPS);

    // Title card, 0 to INTRO_DUR
    var titlePos = [WIDTH * INTRO_CENTER[0], HEIGHT * INTRO_CENTER[1]];
    var credit = makeMadd(comp, INTRO_CREDIT, px(CREDIT_SIZE), "00 Credit", fontPS, WIDTH * INTRO_MAX_WIDTH, tatweelPerPx);
    var title = makeMadd(comp, INTRO_TITLE, px(TITLE_SIZE), "00 Title", fontPS, WIDTH * INTRO_MAX_WIDTH, tatweelPerPx);
    title.inPoint = 0; title.outPoint = INTRO_DUR;
    credit.inPoint = 0; credit.outPoint = INTRO_DUR;
    var titleH = centreAt(title, titlePos);
    var creditH = rectOf(credit).height;
    var creditPos = [titlePos[0], titlePos[1] + titleH / 2 + px(CREDIT_GAP) + creditH / 2];
    centreAt(credit, creditPos);

    addReveal(title, 0.3, 1.3);
    addGlint(title, 2.0, 1.4);
    addHoldAndOut(title, titlePos, 0, INTRO_DUR, 106);
    var titleScale = tr(title, "ADBE Scale");               // settle from 106% by 2.2 s, then the slow push
    titleScale.setValueAtTime(2.2, [100, 100, 100]);
    easeKeys(titleScale);
    addReveal(credit, 1.3, 1.0);
    addHoldAndOut(credit, creditPos, 0, INTRO_DUR, 100);
    addMarker(comp, 0, plain(INTRO_TITLE));

    // Lyrics, PHRASE_DUR each
    var lyricPos = [WIDTH * LYRIC_CENTER[0], HEIGHT * LYRIC_CENTER[1]];
    for (var n = 0; n < LYRICS.length; n++) {
        var t0 = INTRO_DUR + n * PHRASE_DUR;
        var t1 = t0 + PHRASE_DUR;
        var num = (n + 1 < 10 ? "0" : "") + (n + 1);
        var line = makeMadd(comp, LYRICS[n], px(LYRIC_SIZE), num + " " + plain(LYRICS[n]), fontPS,
                            WIDTH * LYRIC_MAX_WIDTH, tatweelPerPx);
        line.inPoint = t0;
        line.outPoint = t1;
        centreAt(line, lyricPos);
        addReveal(line, t0, IN_DUR);
        addHoldAndOut(line, lyricPos, t0, t1, 100);
        addMarker(comp, t0, num + "  " + plain(LYRICS[n]));
    }

    if (ADD_TO_RENDER_QUEUE) {
        try {
            var rq = app.project.renderQueue.items.add(comp);
            var om = rq.outputModule(1);
            var templates = om.templates, template = null;
            for (var t = 0; t < templates.length; t++) {
                if (templates[t] === "High Quality with Alpha") template = templates[t];
            }
            for (var u = 0; !template && u < templates.length; u++) {
                if (templates[u].indexOf("Alpha") >= 0) template = templates[u];
            }
            if (template) om.applyTemplate(template);
        } catch (e) {}
    }

    comp.openInViewer();
    app.endUndoGroup();

    var msg = COMP_NAME + ": " + total + " s, " + WIDTH + "x" + HEIGHT + ", " + FPS + " fps, transparent.\n" +
              "Title card 0-" + INTRO_DUR + " s, then " + LYRICS.length + " lines of " + PHRASE_DUR + " s.\n\n";
    msg += chosen ? "Font: " + chosen.label + " (" + chosen.ps + ")" :
                    "None of these fonts is installed: " + FONTS.join(", ") +
                    ". The text uses After Effects' default font; put an installed Arabic font first in FONTS.";
    msg += "\n\nIf the Arabic letters look disconnected: Preferences > Type > Text Engine > " +
           "South Asian and Middle Eastern, restart After Effects, run again.";
    alert(msg);
})();

// HH — switch the font on every text layer of the lyrics comp (File > Scripts > Run Script File...)
// Asks for a font (family, full name or PostScript name), applies it to all text layers in the active comp
// (or the comp named HH_Lyrics), and re-centres each line so the layout stays centred.
// For a full rebuild with the new font, change FONT at the top of HH_Lyrics_AE.jsx and run that instead.
// Keep this file saved as UTF-8 (with BOM).

(function HH_Lyrics_SetFont() {

    var COMP_NAME = "HH_Lyrics";
    var DEFAULT_FONT = "ديوان مد";

    function lower(s) { return String(s).toLowerCase(); }

    function fontField(f, key) {
        try { return f[key] ? String(f[key]) : ""; } catch (e) { return ""; }
    }

    function isRegular(f) {
        var s = lower(fontField(f, "styleName"));
        return s === "regular" || s === "normal" || s === "book" || s === "medium";
    }

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
        eachFont(function (f) {
            for (var k = 0; k < fields.length; k++) {
                var v = lower(fontField(f, fields[k]));
                if (!v) continue;
                if (v === key) { if (!exact || isRegular(f)) exact = f; }
                else if (!partial && v.indexOf(key) >= 0) partial = f;
            }
        });
        return exact || partial;
    }

    var comp = app.project ? app.project.activeItem : null;
    if (!(comp && comp instanceof CompItem)) {
        comp = null;
        for (var i = 1; app.project && i <= app.project.numItems; i++) {
            var item = app.project.item(i);
            if (item instanceof CompItem && item.name === COMP_NAME) { comp = item; break; }
        }
    }
    if (!comp) { alert("Open the " + COMP_NAME + " comp first."); return; }

    var name = prompt("Font for all text layers in \"" + comp.name + "\"\n(family, full name or PostScript name):",
                      DEFAULT_FONT);
    if (!name) return;
    var font = findFont(name);
    var fontPS = font ? fontField(font, "postScriptName") : name;

    app.beginUndoGroup("HH set font");
    var changed = 0, failed = 0, wide = [];
    for (var n = 1; n <= comp.numLayers; n++) {
        var layer = comp.layer(n);
        if (!(layer instanceof TextLayer)) continue;
        var prop = layer.property("ADBE Text Properties").property("ADBE Text Document");
        var td = prop.value;
        try { td.font = fontPS; prop.setValue(td); changed++; } catch (e) { failed++; continue; }
        // Re-centre at the middle of the layer's time, when its animators are at rest.
        var t = (layer.inPoint + layer.outPoint) / 2;
        var r = layer.sourceRectAtTime(t, false);
        layer.property("ADBE Transform Group").property("ADBE Anchor Point").setValue([r.left + r.width / 2, r.top + r.height / 2]);
        if (r.width > comp.width * 0.9) wide.push(layer.name);
    }
    app.endUndoGroup();

    var msg = "Font set on " + changed + " text layers: " + fontPS +
              (font ? "" : "\n(not found by name in the font list; After Effects used it only if it recognises it)");
    if (failed) msg += "\n" + failed + " layers could not take this font.";
    if (wide.length) msg += "\n\nThese lines are now wider than 90% of the frame; reduce their size or run " +
                            "HH_Lyrics_AE.jsx with this font to refit them:\n" + wide.join("\n");
    msg += "\n\nThe credit's distance under the title is set for the original font; run HH_Lyrics_AE.jsx " +
           "again with this font for an exact layout.";
    alert(msg);
})();

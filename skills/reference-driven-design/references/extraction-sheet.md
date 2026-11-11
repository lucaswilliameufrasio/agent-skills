# Reference extraction sheet

Fill one sheet per reference. Write values, not adjectives. Mark every value as
`measured` (sampled from pixels or source) or `estimated` (read by eye).

```markdown
## Reference <letter>: <short name>

- Source: <URL or file path>, consulted <YYYY-MM-DD>
- Viewport / device: <e.g. 1440×900 desktop, 390×844 phone>
- Role: <what this reference is for, e.g. "density and tables">

### Layout
- Grid / columns:
- Max content width:
- Alignment (left / centered / mixed):
- Section separation (space / rule / background change):
- Density (rows or items visible per screen):

### Spacing
- Base unit:
- Common gaps (inside components / between groups / between sections):

### Typography
- Families (classification, name if identifiable):
- Size steps (px) and line heights:
- Weights in use:
- Case and tracking (labels, headings):
- Numerals (tabular / proportional):

### Color
| Role | Value | measured/estimated |
| --- | --- | --- |
| background | | |
| surface | | |
| border | | |
| text primary | | |
| text secondary | | |
| accent (where used) | | |
| status | | |
- Share of screen that is colored (roughly):

### Shape and depth
- Radius by element (buttons, inputs, containers, images):
- Borders vs shadows vs fills:
- Elevation steps:

### Components seen
- <component>: anatomy, sizes, visible states

### Icons and imagery
- Icon style (stroke/fill, weight, size):
- Imagery (photo / illustration / none):

### Signature moves (2–4)
1.
2.

### Do not take
- <logo, illustration, copy, identifying composition>
```

## Sampling colors from an image

Prefer real pixel values over guesses. Use whatever is already available, for
example an image editor's picker, ImageMagick
(`magick ref.png -crop 1x1+X+Y txt:-`), or Python with Pillow
(`Image.open(path).convert("RGB").getpixel((x, y))`). Screenshots can be scaled
or compressed, so sample flat areas away from edges and anti-aliased text.

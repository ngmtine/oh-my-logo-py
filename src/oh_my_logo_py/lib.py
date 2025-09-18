from . import palettes, renderer


def oh_my_logo(
    text: str,
    palette_name: str = "grad-blue",
    font: str = "standard",
    filled: bool = False,
) -> None:
    """
    ロゴを生成し、コンソールに表示します

    Args:
        text: 表示するテキスト
        palette_name: 使用するカラーパレット名
        font: 使用するfiglet/cfontsフォント名
        filled: 塗りつぶしモードを使用するかどうか
    """

    palette = palettes.resolve_palette(palette_name)
    if palette is None:
        print(f"Warning: Palette '{palette_name}' not found. Using default.")
        palette = palettes.get_default_palette()

    render_palette = palette
    transition = True

    colored_logo = renderer.render_logo(
        text=text,
        palette=render_palette,
        font=font,
        filled=filled,
        transition=transition,
    )

    if colored_logo:
        print(colored_logo)

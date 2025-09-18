import pyfiglet
from cfonts import render as cfonts_render

# ANSIエスケープコード
ESC = "\x1b"
RESET = f"{ESC}[0m"


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """HEXカラーコードをRGBタプルに変換します"""

    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)


def rgb_to_ansi_truecolor(
    rgb: tuple[int, int, int],
    background: bool = False,
) -> str:
    """RGBタプルをANSI TrueColor (24-bit) のエスケープシーケンスに変換します"""

    r, g, b = rgb
    code = 48 if background else 38
    return f"{ESC}[{code};2;{r};{g};{b}m"


def create_gradient(
    palette: list[str],
    steps: int,
) -> list[tuple[int, int, int]]:
    """色のリスト（パレット）から、指定したステップ数のグラデーション（RGBタプルのリスト）を生成します"""

    gradient: list[tuple[int, int, int]] = []
    if not palette or steps <= 0:
        return []
    if len(palette) == 1:
        return [hex_to_rgb(palette[0])] * steps

    rgb_palette = [hex_to_rgb(c) for c in palette]
    num_segments = len(rgb_palette) - 1
    if num_segments <= 0:
        return [rgb_palette[0]] * steps

    steps_per_segment = steps // num_segments
    extra_steps = steps % num_segments

    for i in range(num_segments):
        start_color, end_color = rgb_palette[i], rgb_palette[i + 1]
        current_steps = steps_per_segment + (1 if i < extra_steps else 0)
        if current_steps == 0:
            continue

        for j in range(current_steps):
            ratio = j / (current_steps - 1) if current_steps > 1 else 0
            r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
            gradient.append((r, g, b))

    return gradient


def render_logo(
    text: str,
    palette: list[str],
    font: str = "standard",
    filled: bool = False,
    transition: bool = False,
) -> str:
    """
    テキストをアスキーアートに変換し、文字列として返します
    `filled`がTrueの場合はcfontsを、Falseの場合はpyfigletを使用します
    """

    if filled:
        return cfonts_render(text, font=font, gradient=palette, transition=transition)
    else:
        # pyfigletは文字列を返す
        try:
            ascii_art = pyfiglet.figlet_format(text, font=font.lower())
        except pyfiglet.FontNotFound:
            ascii_art = pyfiglet.figlet_format(text, font="standard")

        lines = ascii_art.split("\n")
        non_empty_lines = [line for line in lines if line.strip()]
        if not non_empty_lines:
            return ascii_art

        gradient_colors = create_gradient(palette, len(non_empty_lines))

        colored_lines: list[str] = []
        color_index = 0
        for line in lines:
            if line.strip() and color_index < len(gradient_colors):
                color = gradient_colors[color_index]
                ansi_color = rgb_to_ansi_truecolor(color)
                colored_lines.append(f"{ansi_color}{line}{RESET}")
                color_index += 1
            else:
                colored_lines.append(line)

        return "\n".join(colored_lines)

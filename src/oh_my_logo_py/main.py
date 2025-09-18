import argparse

from .lib import oh_my_logo
from .palettes import get_palette_names


def main():
    """CLIのエントリーポイント"""

    parser = argparse.ArgumentParser(
        description="Display a logo in the terminal with a gradient color.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "text",
        nargs="?",
        default="oh-my-logo",
        help="The text to display. Defaults to 'oh-my-logo'.",
    )
    parser.add_argument(
        "-p",
        "--palette",
        help="The color palette to use.",
    )
    parser.add_argument(
        "-f",
        "--font",
        help="The font to use (for pyfiglet or cfonts).",
    )
    parser.add_argument(
        "--list-palettes",
        action="store_true",
        help="List all available palettes and exit.",
    )
    parser.add_argument(
        "--filled",
        action="store_true",
        help="Use filled characters via cfonts.",
    )
    parser.add_argument(
        "--gallery",
        action="store_true",
        help="Render text in all available palettes.",
    )

    args = parser.parse_args()

    if args.list_palettes:
        print("Available palettes:")
        for name in get_palette_names():
            print(f"- {name}")
        return

    # --filled オプションに応じてデフォルトのフォントを決定
    if args.filled:
        font = args.font if args.font is not None else "block"
    else:
        font = args.font if args.font is not None else "standard"

    # --gallery オプションの処理
    if args.gallery:
        all_palettes = get_palette_names()
        for palette_name in all_palettes:
            print(f"\n--- {palette_name.upper()} ---\n")
            oh_my_logo(
                text=args.text,
                palette_name=palette_name,
                font=font,
                filled=args.filled,
            )
        return

    # 通常のロゴ表示
    palette_name = args.palette
    if palette_name is None:
        palette_name = "mono" if args.filled else "grad-blue"

    oh_my_logo(text=args.text, palette_name=palette_name, font=font, filled=args.filled)


if __name__ == "__main__":
    main()

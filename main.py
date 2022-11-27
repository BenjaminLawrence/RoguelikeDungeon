#!/usr/bin/env python3
import tcod


def main() -> None:
    screen_width = 80
    screen_height = 50

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        title="Roguelike Dungeon",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=1, y=1, string="@")

            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()
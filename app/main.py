import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) == 3 and command_parts[0].lower() == "mv":
        source_path = command_parts[1]
        dest_path = command_parts[2]

        if dest_path.endswith("/"):
            dir_path = dest_path
            filename = source_path.split("/")[-1]
            final_dest_path = dir_path + filename
        else:
            final_dest_path = dest_path

            if "/" in dest_path:
                dir_path = "/".join(dest_path.split("/")[:-1])
            else:
                dir_path = ""

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with (
            open(source_path, "r") as f_source,
            open(final_dest_path, "w") as f_dest
        ):
            f_dest.write(f_source.read())

        os.remove(source_path)

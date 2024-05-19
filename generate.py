import os
import glob
import markdown

def generate(work_dir):
    # Get current working directory
    # cwd = os.getcwd()
    start_dir = os.getcwd()
    cwd = work_dir
    directories = cwd.split(os.sep)
    out_filename = directories[-2] + '.md'

    # Create an empty string to hold all markdown contents after "---"
    all_contents = ""

    # Get all subdirectories in current working directory
    subdirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]

    # Loop through each subdirectory
    for subdir in subdirs:
        # Change current working directory to subdirectory
        os.chdir(os.path.join(cwd, subdir))

        # Find all markdown files in current subdirectory
        md_files = glob.glob("*.md")

        # Loop through each markdown file
        for filename in md_files:
            with open(filename, "r") as file:
                content = file.read()
                parts = content.split("---")
                all_contents += parts[-1]

    # Apply markdown formatting to the concatenated text
    formatted_text = markdown.markdown(all_contents, extras=['fenced-code-blocks'])

    # Write the formatted text to a new markdown file in the directory the script was run from.
    with open(os.path.join(start_dir, out_filename), "w") as file:
        file.write(formatted_text)

    # Change current working directory back to original directory
    os.chdir(cwd)
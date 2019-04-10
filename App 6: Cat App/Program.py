import os
import cat_service
import subprocess


def main():
    print_header()
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('-------------------')
    print('    cat factory')
    print('-------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    print('Displaying cats in OS window.')
    subprocess.call(['open', folder])


if __name__ == '__main__':
    main()

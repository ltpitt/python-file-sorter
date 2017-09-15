import os
import click

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0']


def create_folders(path, folder_group_size):
    os.chdir(path)
    folder_groups = [[''.join(letters[letter:letter + folder_group_size])] \
                     for letter in range(0, len(letters), folder_group_size)]
    folder_groups.insert(0, numbers)
    for folder_group in folder_groups:
        folder_name = folder_group[0].upper()
        if not os.path.exists(folder_name):
            click.echo('Creating folder: ' + folder_name)
            os.makedirs(folder_name)
    return folder_groups


def get_files(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if (filename[0] != '.' and (not filename.endswith('.py') \
                                                and not filename.endswith('.pyc') \
                                                and not filename.endswith('.md') \
                                                and not filename.startswith('LICENSE'))):
                files.append(filename)
    return files


def move_files_in_folders(path, source_files, destination_folders):
    moved_files_counter = 0
    skipped_files_counter = 0
    for file in source_files:
        if file[0].isnumeric():
            filename_first_character = '0'
        else:
            filename_first_character = file[0].upper()
        source_file_path = os.path.join(path + '/' + file)
        for folder in destination_folders:
            folder = folder[0].upper()
            if filename_first_character in folder:
                destination_file_path = os.path.join(path + '/' + folder + '/' + file)
                if not os.path.isfile(destination_file_path):
                    click.echo('Moving: ' + source_file_path + ' to: ' + destination_file_path)
                    os.rename(source_file_path, destination_file_path)
                    moved_files_counter += 1
                else:
                    click.echo('File: ' + source_file_path + ' already exists in: ' + destination_file_path)
                    skipped_files_counter += 1
    click.echo()
    click.echo('Process is complete.')
    click.echo()
    click.echo('Moved ' + str(moved_files_counter) + ' files')
    click.echo('Skipped ' + str(skipped_files_counter) + ' files')


@click.command()
@click.option('--path', default='.', help='Path where the sorting will be applied', required=True)
@click.option('--folder_group_size', default=1,
              help='Number of letters that will be grouped into a single folder e.g. 3 will create folders: 0 ABC DEF GHI ...')
def main(path, folder_group_size):
    click.echo('Ready to move files all files from: ' + str(path) +
               ' to directories that will be created in the same path' )
    if click.confirm('Do you want to continue?'):
        click.echo('Rock\'n\'roll!')
        created_folders = create_folders(path, folder_group_size)
        files = get_files(path)
        if len(files) > 0:
            move_files_in_folders(path, files, created_folders)
    else:
        click.echo('Ok, bye!')

# Uncomment those rows for manual testing
#if __name__ == '__main__':
#    main()

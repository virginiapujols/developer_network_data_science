
def get_files_per_developer(repo):
    files_to_developer_dict = dict()
    for commit in list(repo.iter_commits('master')):
        author_email = commit.committer.email
        files = list(commit.stats.files.keys())
        for file in files:
            if file in files_to_developer_dict:
                files_to_developer_dict[file].add(author_email)
            else:
                files_to_developer_dict[file] = {author_email}

    print('{} files saved!'.format(len(files_to_developer_dict.keys())))
    return files_to_developer_dict


def create_nodes_connection(dev_email1, dev_email2, dev_network_set):
    # Validate if the connection exists already
    connection1 = "{} : {}".format(dev_email1, dev_email2)
    connection2 = "{} : {}".format(dev_email2, dev_email1)
    filtered_connections = list(filter(lambda e: (e == connection1 or e == connection2), dev_network_set))

    if len(filtered_connections) > 0:
        return None

    # Otherwise, return the string with format "email1:email2"
    value = dev_email1 + " : " + dev_email2
    print(value)
    return value


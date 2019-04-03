import git
from git import Repo


def get_repo_local(project_path):
    repo = Repo(project_path)
    is_empty = repo.bare
    print('Is repo empty? ', is_empty)
    assert not is_empty
    return repo


def get_repo_remote():
    try:
        remote_path = '{git_remote}'
        local_path = '{path}'
        Repo.clone_from(f'{remote_path}', f'{local_path}/')
    except git.exc.GitError:
        print(f'ERROR!')


def get_committer_list(repo):
    committer_set = set()
    for commit in list(repo.iter_commits('master')):
        committer_set.add(commit.committer.email)
    print('\n'.join(list(committer_set)))
    return list(committer_set)

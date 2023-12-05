from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("")

# Public Web Github
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)
print()

for repo in g.get_user().get_repos():
    try:
        if("PROGI PROJEKT 2023" in (str(repo.get_readme().decoded_content).upper())):
            print("repo name: " + repo.name)
            if(repo.license is None):
                print("Repo: "+repo.name+" has no license")
                nl=False
                for issue in repo.get_issues():
                    if(issue.title=="Nema Licence"):
                        nl=True
                        break
                if(not nl):
                    repo.create_issue(title="Nema Licence", body="Di je Licenca", labels=["documentation"])
        else:
            print("repo name: " + repo.name + " has no PROGI PROJEKT 2023")
    except:
        print("repo name: " + repo.name + " has no README.md")

#stvari za branchove
# for branch in branches:
#     print(branch.name)

# contents = repo.get_contents("", ref=repo.get_branch("master").name)
# while contents:
#     file_content = contents.pop(0)
#     if file_content.type == "dir":
#       contents.extend(repo.get_contents(file_content.path, ref=repo.get_branch("master").name))
#     else:
#       print(file_content)

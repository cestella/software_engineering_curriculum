# Software Engineering Curriculum

The following repository is a series of software engineering problems,
which should be completed in Python 3. These exercises are intended to
grow you as an budding engineer. Some exercises will be broad and some
will be small.  Some will be broken down in a fine-grain and some will
be very broad.

## Rules
There are a few rules for this repository:
1. You are expected to use `git` and `vim` directly from the terminal
2. All solutions (unless otherwise indicated) should be in Python 3
3. You may *not* directly commit changes to `master`, rather submit pull requests against `master` and request a review.

## Pull Request Primer

You are expected to be somewhat comfortable with `git` at this point,
but in the case that you are *not* entirely comfortable, the following
section will briefly cover `git` to the level that you require to do
function in this repository.

The unit of work for a reviewable solution is a Feature.  Every Feature
should have the following associated with it:
* A branch of the form `wastella/<name>` (e.g. `wastella/my_fancy_feature`)
* A Pull Request (visible in the `Pull Requests` Tab above)

Therefore, the creation of a feature involves the following steps:
1. Create a local branch of the form `wastella/<name>`
2. Make some changes
3. Commit those changes locally
4. If satisfied that this fully implements the feature as stated, goto 5
   otherwise goto 2
5. Push the local branch with those commits to a remote branch
6. Create a Pull Request

Let's see this in action here:
```
# Notice that I'm in the `master` branch as my command line tells me
# I'm going to create a new branch, cstella/initial_instructions
{23:03}~/code/william/software_engineering_curriculum:master ✓ ➭ git checkout -b cstella/initial_instructions
Switched to a new branch 'cstella/initial_instructions'
# Now my command line tells me that I'm in cstella/initial_instructions (whereas before it said master)
# I have 2 files in the repository right now.  I'm going to edit the README
{23:04}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✓ ➭ ls
LICENSE   README.md
# Editing the README.md (this file that you're viewing right now!)
{23:04}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✓ ➭ vi README.md
# Notice that there's a little x on my command line.  This indicates there are changes locally that haven't been committed to my branch
{23:19}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✗ ➭ git add .
# I will use `git status` to tell me what has been modified
{23:19}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✗ ➭ git status
On branch cstella/initial_instructions
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
# I'm just going to commit everything by using `git commit -a`
# Furthermore, I'll just specify the commit message right on the command
# line by using `-m` followed by my message (remember to put it in double quotes)
{23:19}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✗ ➭ git commit -a -m "First cut of the readme"
[cstella/initial_instructions c3a82c8] First cut of the readme
 1 file changed, 35 insertions(+), 2 deletions(-)
 rewrite README.md (100%)
# Now I can push my changes to create a remote branch in my repo.
# This involves setting the upstream to `origin` and pushing my branch
{23:19}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✓ ➭ git push --set-upstream origin cstella/initial_instructions
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1011 bytes | 1011.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'cstella/initial_instructions' on GitHub by visiting:
remote:      https://github.com/cestella/software_engineering_curriculum/pull/new/cstella/initial_instructions
```
Note at the end, it specifies the URL to go to in your web browser to
make the pull request.  If you go to that URL, you can follow the
instructions to create a PR.  Another way to create the PR is to go to
https://github.com/cestella/software_engineering_curriculum and there
should be a section that says "Your recently pushed branches:".  Under
that section, there is a button called `Compare & pull request`.  You
can click that.

## `git` Primer

Git can be complex, so let's go through some of the common commands and
when to use them.

### `git checkout`

`git checkout` has two main purposes, either creating a local branch
(using the `-b` argument) or switching to an existing branch.

For instance:
```
# Create a new branch called `cstella/my_branch`
git checkout -b cstella/my_branch
# Switch to `master`
git checkout master
```

One thing to note about switching branches; git will let you know if you
have changes which you have staged but not committed.  Please either
commit them or revert the change.

### `git add/status`

Adding changes to a commit and seeing what changes are part of a commit.
The act of adding a file which was changed to a commit is called
`staging` a commit.

```
# Add a file `foo.py` to a commit
git add foo.py
# Add all files that are modified recursively from the current directory
git add .
# See what files are staged and which are not (I have modified one file, README.md
git status
On branch cstella/initial_instructions
Your branch is up to date with 'origin/cstella/initial_instructions'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

### `git commit`

Committing a staged commit (see the section on `git add/status`) is the
act of adding a change to your local branch.  This is done via `git
commit` and it has various arguments which you may be interested in
using.  I'll go over some relevant ones:
* `-a` will stage all modified files into the commit.
* `-m` will allow you to specify the git commit message.  If this isn't used, `vim` will be opened up so you can type out a commit message there.  Remember that the argument here should be wrapped in double-quotes. For instance `git commit -m "This commit fixes a bug"`

### `git push --set-upstream`

Pushing a branch in `git` will push a set of commits to a remote branch.
Merely creating a branch via `git checkout -b <branch_name>` will only
create a local branch, which you can commit changes to (via `git
commit`).  In order to make that local change known to github, you must
push the local branch to the repository via `git push --set-upstream
origin <branch_name>` (e.g. `git push --set-upstream origin
wastella/my_feature`).  If you are curious, `--set-upstream` informs `git`
that you want to push to a remote repository called `origin`.  `origin`
is the name of the repository that you cloned initially.

### Adding a new commit

Of course, pushing your local branch to the repository is only required
once.  Once it's pushed, it's there, but you may want to add
some commits to it.  For instance, maybe you submit a pull request and
your reviewer asks for changes.  In that case, you can merely commit
your change (see the section above on `git commit`) and then merely `git push`.

For instance, consider this session where I am adding a change to this document, committing the change and pushing the change to my already remote branch:
```
{23:47}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✗ ➭ git status
On branch cstella/initial_instructions
Your branch is up to date with 'origin/cstella/initial_instructions'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
{23:47}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✗ ➭ git add .
{23:47}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✗ ➭ git commit -a -m "Added a new section on git primer"
[cstella/initial_instructions 8e485c0] Added a new section on git primer
 1 file changed, 128 insertions(+), 1 deletion(-)
{23:47}~/code/william/software_engineering_curriculum:cstella/initial_instructions ✓ ➭ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 3.09 KiB | 3.09 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:cestella/software_engineering_curriculum.git
   c3a82c8..8e485c0  cstella/initial_instructions -> cstella/initial_instructions
```

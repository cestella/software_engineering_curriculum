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

## `git` Primer

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


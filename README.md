1. Navigate to Your Local Repository
	Open your terminal and navigate to the root directory of your local repository:
		cd ~/Documents/leetcode-solutions/leetcode-solutions

2. Add the New File to Git
	Use the git add command to stage the new file::
		git add Arrays-and-Hashing/Easy/remove_element.py

3. Commit the Changes
	Write a commit message describing the changes:
		git commit -m "Solution for 'Remove Element' problem"

4. Push the Changes to GitHub
	Push the changes to the remote repository on GitHub:
		git push origin main

5. Verify on GitHub
	Visit your GitHub repository in your browser to confirm that remove_element.py has been added under the correct directory.




Example:

i: ls

i: cd Documents

i: ls

i: cd leetcode-solutions

i: ls

i: cd leetcode-solutions

i: ls

o: Arrays-and-Hashing

i: ls -a

o: .			..			.git			Arrays-and-Hashing

i: git add Arrays-and-Hashing/Easy/remove_element.py

i: git commit -m "Solution for 'Remove Element' problem"

o:[main] Solution for 'Remove Element' problem
 1 file changed, 64 insertions(+)
 create mode 100644 Arrays-and-Hashing/Easy/remove_element.py

i: git push origin main

o: Enter passphrase for key '/Users/___________________/.ssh/id_xxxxxxx': 

""" ************************************************************************** """

If it appears that multiple changes were mistakenly grouped under the same commit in your GitHub repository, and you need to split these into separate commits under unique messages follow the steps sequentaily below.

E.g.: The current interactive rebase (git rebase -i HEAD~3) does not show all the files or commits you expect, suggesting that some changes might have been squashed or merged together in the history.

If there are multiple commits with the same commit message:
1. Start Interactive Rebase for Commit to Split: 
	Since the files you mentioned are all part of the commit d58bebc (the last one in your git rebase -i HEAD~3 list), start by rebasing to that point:
		git rebase -i HEAD~3'

2. Mark the Commit to Edit: In the editor that opens, change the word 'pick' to 'edit' for the commit where the changes are grouped (e.g., d58bebc):
	Save and close the editor:
		Press Ctrl + O
		Press Enter
		Press Ctrl + X

3. Unstage the Changes: After Git pauses the rebase, unstage all the changes in the selected commit:
	git reset HEAD^
		This will leave the changes from d58bebc in your working directory without committing them.

4. Commit Each File Separately: For each file, create a new commit with the correct message. For example: 
	git add roman_to_integer.py
	git commit -m "Solution for 'Roman to Integer' problem"

	git add remove_element.py
	git commit -m "Solution for 'Remove Element' problem"

	git add remove_duplicates.py
	git commit -m "Solution for 'Remove Duplicates' problem"

5. Continue the Rebase: Once you've created separate commits for each file, continue the rebase:
	git rebase --continue

6. Force Push the Updated History: Since this rewrites commit history, force push to update the remote repository:
	git push --force

Summary:
	Why This Works
		This process effectively splits the combined commit (d58bebc) into multiple smaller commits, each associated with the specific file and a unique commit message. By doing this, your GitHub repository will reflect the correct history where each file has its own descriptive commit.





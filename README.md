<!DOCTYPE html>
<html>
<body>
	<h1> My Git Tutorial Notes </h1>
		<h3>1. Navigate to Your Local Repository</h3>
		<p>Open your terminal and navigate to the root directory of your local repository:</p>
		<pre><code>
		cd ~/Documents/leetcode-solutions/leetcode-solutions
	  </code></pre>
		<h3> 2. Add the New File to Git </h3>
		<p>Use the git add command to stage the new file:</p>
	  <pre><code>
		git add Arrays-and-Hashing/Easy/remove_element.py
	  </pre></code>
		<h3>3. Commit the Changes</h3>
		<p>Write a commit message describing the changes:</p>
		<pre><code>
		git commit -m "Solution for 'Remove Element' problem"
		</code></pre>
		<h3>4. Push the Changes to GitHub</h3>
		<p>Push the changes to the remote repository on GitHub:</p>
		<pre><code>
		git push origin main
		</code><pre>
		<h3>5. Verify on GitHub</h3>
	Visit your GitHub repository in your browser to confirm that remove_element.py has been added under the correct directory.

Example:

i: ls

i: cd Documents

i: ls

i: cd leetcode-solutions

i: ls

i: cd leetcode-solutions

i: ls <br>
o: Arrays-and-Hashing

i: ls -a <br>
o: .			..			.git			Arrays-and-Hashing

i: git add Arrays-and-Hashing/Easy/remove_element.py

i: git commit -m "Solution for 'Remove Element' problem" <br>
o:[main] Solution for 'Remove Element' problem <br>
1 file changed, 64 insertions(+) <br>
create mode 100644 Arrays-and-Hashing/Easy/remove_element.py

i: git push origin main <br>
o: Enter passphrase for key '/Users/___________________/.ssh/id_xxxxxxx': 

""" ********************************************************************************************************************************* """

If it appears that multiple changes were mistakenly grouped under the same commit in your GitHub repository, and you need to split these into separate commits under unique messages follow the steps sequentaily below. <br>
E.g.: The current interactive rebase (git rebase -i HEAD~3) does not show all the files or commits you expect, suggesting that some changes might have been squashed or merged together in the history.

If there are multiple commits with the same commit message:
1. Start Interactive Rebase for Commit to Split: 
	Since the files you mentioned are all part of the commit d58bebc (the last one in your git rebase -i HEAD~3 list), start by rebasing to that point: <br>
		git rebase -i HEAD\~3

2. Mark the Commit to Edit: In the editor that opens, change the word 'pick' to 'edit' for the commit where the changes are grouped (e.g., d58bebc):
	Save and close the editor: <br>
		Press Ctrl + O <br>
		Press Enter <br>
		Press Ctrl + X 

3. Unstage the Changes: After Git pauses the rebase, unstage all the changes in the selected commit: <br>
	This will leave the changes from d58bebc in your working directory without committing them. <br>
 		git reset HEAD^
		

4. Commit Each File Separately: For each file, create a new commit with the correct message. <br> For example: <br> 
	git add roman_to_integer.py <br> 
	git commit -m "Solution for 'Roman to Integer' problem" <br><br>
	git add remove_element.py <br>
	git commit -m "Solution for 'Remove Element' problem" <br><br> 
	git add remove_duplicates.py <br> 
	git commit -m "Solution for 'Remove Duplicates' problem" <br> 

5. Continue the Rebase: Once you've created separate commits for each file, continue the rebase: <br>
	git rebase --continue

6. Force Push the Updated History: Since this rewrites commit history, force push to update the remote repository: <br>
	git push --force
<br><br><br>
Summary:<br><br>
	Why This Works?<br>
		This process effectively splits the combined commit (d58bebc) into multiple smaller commits, each associated with the specific file and a unique commit message. By doing this, your GitHub repository will reflect the correct history where each file has its own descriptive commit.

	</body>
</html>



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

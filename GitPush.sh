git init
git add .
echo "What is the remote origin?: "
read remote_origin
git remote add origin $remote_origin
echo "Commit text: "
read commit_text
git commit -m $commit_text
git push -u origin masterx
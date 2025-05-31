#!/bin/bash


mkdir -p ~/Final

touch ~/File1 ~/File2 ~/File3 ~/File4


for i in 1 2 3 4; do
  echo -e "This is line one of file $i\nThis is line two of file $i\nThis is line three of file $i" > ~/File$i
done


cp ~/File{1,2,3,4} ~/Final/


for file in ~/Final/File*; do
  echo "----- Contents of $(basename "$file") -----"
  cat "$file"
  echo ""
done


read -p "Enter the name of a file in your home directory: " filename



filepath=~/"$filename"
if [[ -f "$filepath" ]]; then
  echo "----- Contents of $filename -----"
  cat "$filepath"
else
  echo "File '$filename' does not exist in your home directory."
fi

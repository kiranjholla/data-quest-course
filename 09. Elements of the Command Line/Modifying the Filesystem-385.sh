## 1. Creating Directories ##

/home/dq$ mkdir dir2 dir3 dir5

## 2. Deleting Directories ##

/home/dq$ rmdir dir2 dir3 dir5

## 3. Failing to Delete Directories ##

/home/dq$ ls -A prize_winners/

## 4. Copying Files ##

/home/dq$ cp augustus violet veruca tv brats

## 5. Hidden Dangers of Copying Files ##

/home/dq$ cp -i prize_winners/.mike prize_winners/mike

## 6. Copying Directories ##

/home/dq$ cp -r prize_winners brats/

## 7. Deleting Directories and Files ##

/home/dq$ rm -R prize_winners/

## 8. Moving and Renaming Directories and Files ##

/home/dq$ mv brats/prize_winners/.mike brats/prize_winners/Mike
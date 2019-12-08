## 1. Printing User Input ##

/home/dq$ echo "This is a command line interface."

## 2. Redirecting Output with > ##

/home/dq$ grep -ih ",math" rg_data/* > math_data

## 3. Redirecting Output with >> ##

/home/dq$ head -n 1 rg_data/*

## 4. Creating Empty Files ##

/home/dq$ ls

## 5. Why Pipelines? ##

/home/dq$ wcone

## 6. Using Pipelines ##

/home/dq$ zen | grep -i better

## 7. The Unix Philosophy ##

/home/dq/rg_data$ sort -u * | wc -l

## 8. Trying to Redirect Errors ##

/home/dq/rg_data$ echo "something" > /dev/null
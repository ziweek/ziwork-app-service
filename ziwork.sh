#!/bin/sh





# echo $$

# file_name=$0
# echo ${file_name}
# all_param=$*
# echo ${all_param}
# param_length=$#
# echo ${param_length}

# param1=$1
# echo ${param1}
# param2=$2
# echo ${param2}
# param3=$3
# echo ${param3}
 
#  echo -n 'NAME : '
#  read NAME

# echo "Hello, $NAME"
# if [ -e "./.env" ];then
#  echo "file exist"
#  value=`cat ./.env"`
#  echo "$value"
#  less -N "./.env"
# fi



### STATUSCODEs
status200() {
  echo -e "\033[32m...Sucessfully Done!\033[0m"
}

status201() {
  echo -e "\033[32m...Sucessfully Done!\033[0m"
}

error400() {
  echo -e "\033[31m'$1' is not a ziwork command.\033[0m" 
}

error404() {
  echo -e "\033[31mNot Found.\033[0m" 
}



### METHOD
conform() {
  echo -n -e "\033[33mAre you sure? [y/n]: \033[0m"
  read answer
  if [ ${answer} = 'y' ]
  then
    return 1
  else
    return 0
  fi
}

sendEmail() {
  # echo "This is func sendEmail"
  echo -n -e "\033[33mTO : \033[0m"
  read TO
  echo -n -e "\033[33mTITLE : \033[0m"
  read TITLE
  echo -e "\033[33mCONTENT : \033[0m" 
  vim email.template.txt
  echo ---
  while read line; do 
    echo $line 
  done < email.template.txt
  echo ---
  rm -rf email.template.txt
  conform
  if [ $? -eq 1 ]
  then
    status201
  fi
}

addSchedule() {
  echo -n -e "\033[33mTITLE : \033[0m"
  read TITLE
  echo -n -e "\033[33mDATE : \033[0m"
  read DATE
  conform
  if [ $? -eq 1 ]
  then
    status201
  fi
}



### CRUD
get() {
  echo "This is func get"
}

post() {
  # echo "This is func post"
  # if [ -z $1 ]
  # then
  #   error400
  if [ $1 = "email" ]
  then
    # echo "input param is email"
    sendEmail
  elif [ $1 = "schedule" ]
  then
    # echo "input param is schedule"
    addSchedule
  else
    error400 $1
  fi
}

# update() {
#   echo "This is func update"
# }

# delete() {
#   echo "This is func delete"
# }

login() {
  echo "This is func login"
  # 
  echo -n -e "\033[33mEMAIL : \033[0m"
  read EMAIL
  echo -n -e "\033[33mPASSWORD : \033[0m"
  read -s PASSWORD
  echo ''
  # 
  curl -X 'GET' 'http://0.0.0.0:5050/'
  RES=1
  if [ ${RES} -eq 1 ]
  then
   status200
  elif [ ${RES} -ne 1 ]
  then
   error404
  fi
}



### main
if [ $1 = "login" ]
then
#  echo "input param is login"
  login
elif [ $1 = "get" ]
then
#  echo "input param is get"
  get
elif [ $1 = "post" ]
then
  post $2
# if [ -z $1 ]
# then
  
else
  error400 $1
fi
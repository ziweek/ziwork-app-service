# ziwork-app-service

<img src="./src/screenshot_v1.png">

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white"/>
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white"/>
  <br/>
  <img src="https://img.shields.io/badge/Google-4285F4?style=flat-square&logo=Google&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=OpenAI&logoColor=white"/>
  <img src="https://img.shields.io/badge/Naver-03C75A?style=flat-square&logo=Naver&logoColor=white"/>
  <img src="https://img.shields.io/badge/Kakao-FFCD00?style=flat-square&logo=Kakao&logoColor=white"/>
  <br/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Amazon%20AWS-232F3E?style=flat-square&logo=Amazon%20AWS&logoColor=white"/>
</p>
<br/>

## Outline

This application is designed to assist my personal work experience and to make it more efficient.

<br/>

## Goal

- Displaying useful information
- Adding schedule on Google Calender
- Sending email on Gmail
- Logging diary on Database

<br/>

## How it works

### keywords

| keyword | description                        |
| ------- | ---------------------------------- |
| ziwork  | let terminal know statement starts |
| get     |                                    |
| post    |                                    |
| update  |                                    |
| delete  |                                    |
| commit  |                                    |

### tags

| tag | description |
| --- | ----------- |
| -d  | date        |
| -t  | tag         |
| -m  | message     |
| -a  | account     |

<br/>

## Examples

```
$ ziwork post schedule -d 230106 -t univ -m "개설과목공시"
```

```
$ ziwork post email -a austin.jiuk.kim@gmail.com
```

# Reference

| memo                     | link                                                       |
| ------------------------ | ---------------------------------------------------------- |
| Google Calendar API 개요 | https://developers.google.com/calendar/api/guides/overview |
| Gmail API Overview       | https://developers.google.com/gmail/api/guides             |
| openai Playground        | https://beta.openai.com/playground                         |

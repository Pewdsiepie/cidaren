# 更新日志  加入了更多题型适配  填空题自动复制到剪切板  系统资源占用优化2020.4.15 2：19
# 本项目的全部灵感及思路均来自哔哩哔哩[此视频](https://www.bilibili.com/video/BV1R64y1M7q5?from=search&seid=13698410817824032418) 如果觉得此项目对你有帮助，请去该视频下点赞投币收藏三连。



# 由于不知道竞赛请求的URL，所以竞赛的答案只能通过fiddler查看，不能通过exe去方便的打印出来，如果有谁在做竞赛，希望可以在fiddler中查看一下竞赛的url发给我适配一下。


-----------------------------------------------------


# 很抱歉 碍于某些不能说的原因 现在仓库只留下修改后的py文件 和封装后的exe文件  fiddler中的脚本导出路径为c:\cdr\
即fiddler的脚本改为下面的样子
```
    static function OnBeforeResponse(oSession: Session) {
        if(oSession.uriContains("https://wap.vocabgo.com/Student/ClassTask/SubmitAnswer")){
            oSession.utilDecodeResponse();
            oSession.SaveResponse("c:/cdr/response.txt",true);
            oSession.SaveResponseBody("c:/cdr/responseBody.txt");
        }
        if(oSession.uriContains("https://wap.vocabgo.com/Student/StudyTask/SubmitAnswer")){
            oSession.utilDecodeResponse();
            oSession.SaveResponse("c:/cdr/response.txt",true);
            oSession.SaveResponseBody("c:/cdr/responseBody.txt");
        }
        
        
```

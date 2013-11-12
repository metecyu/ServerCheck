用途：
	检查网络服务的连通情况 ，目前支持（url、数据库） 
配置：
	resource/checkItem.xml
	groupname:为配置文件的取一个名称，会在检查界面的标题栏中显示
		只允许配置一个
	urlItem：url检查单元 [root下可配置多个]		
		id:唯一标示号（手动填写）
		title：
		address：url测试地址
		detail：detail
	dbItem：数据库检查单元（目前只支持oracle） [root下可配置多个]
		id：唯一标示号（手动填写）
		title：标题
		ip：数据库服务器ip
		port:端口号
		dbase：sid
		username：用户名
		password：密码
		detail:备注
	-----------------------例子---------------
	<?xml version="1.0" encoding="UTF-8"?>
	<root>
		<groupname>oa系统	</groupname>
		<version>1.0.0</version>
		<urlItem>
			<id>u1</id>
			<title>org组织管理理</title>
			<address>http://172.16.0.166:8080/org/exclude/OrgService.ws</address>
			<detail>deatails</detail>
		</urlItem>
		<urlItem>
			<id>u2</id>
			<title>信息平台</title>
			<address>http://192.0.0.158:8080/XXPT/XxptService.ws</address>
			<detail> urlconfig.xml </detail>
		</urlItem>
		<urlItem>
			<id>u3</id>
			<title>访问授权</title>
			<address>http://172.16.0.166:8080/fwsq/exclude/FwsqService.ws</address>
			<detail> urlconfig.xml </detail>
		</urlItem>
		<urlItem>
			<id>u4</id>
			<title>cas服务器</title>
			<address>https://jgjc.shdrc.gov.cn:8443/cas/login</address>
			<detail>web.xml</detail>
		</urlItem>
		<dbItem>
			<id>d1</id>
			<title>测试数据库</title>
			<type>oracle</type>		
			<ip>172.16.0.112</ip>
			<port>1521</port>
			<dbase>FGWWW1</dbase>
			<username>fgwoa</username>
			<password>fgwoa</password>
			<detail>...</detail>
		</dbItem>
	</root>
	
	
	
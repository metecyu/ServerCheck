��;��
	�������������ͨ��� ��Ŀǰ֧�֣�url�����ݿ⣩ 
���ã�
	resource/checkItem.xml
	groupname:Ϊ�����ļ���ȡһ�����ƣ����ڼ�����ı���������ʾ
		ֻ��������һ��
	urlItem��url��鵥Ԫ [root�¿����ö��]		
		id:Ψһ��ʾ�ţ��ֶ���д��
		title��
		address��url���Ե�ַ
		detail��detail
	dbItem�����ݿ��鵥Ԫ��Ŀǰֻ֧��oracle�� [root�¿����ö��]
		id��Ψһ��ʾ�ţ��ֶ���д��
		title������
		ip�����ݿ������ip
		port:�˿ں�
		dbase��sid
		username���û���
		password������
		detail:��ע
	-----------------------����---------------
	<?xml version="1.0" encoding="UTF-8"?>
	<root>
		<groupname>oaϵͳ	</groupname>
		<version>1.0.0</version>
		<urlItem>
			<id>u1</id>
			<title>org��֯������</title>
			<address>http://172.16.0.166:8080/org/exclude/OrgService.ws</address>
			<detail>deatails</detail>
		</urlItem>
		<urlItem>
			<id>u2</id>
			<title>��Ϣƽ̨</title>
			<address>http://192.0.0.158:8080/XXPT/XxptService.ws</address>
			<detail> urlconfig.xml </detail>
		</urlItem>
		<urlItem>
			<id>u3</id>
			<title>������Ȩ</title>
			<address>http://172.16.0.166:8080/fwsq/exclude/FwsqService.ws</address>
			<detail> urlconfig.xml </detail>
		</urlItem>
		<urlItem>
			<id>u4</id>
			<title>cas������</title>
			<address>https://jgjc.shdrc.gov.cn:8443/cas/login</address>
			<detail>web.xml</detail>
		</urlItem>
		<dbItem>
			<id>d1</id>
			<title>�������ݿ�</title>
			<type>oracle</type>		
			<ip>172.16.0.112</ip>
			<port>1521</port>
			<dbase>FGWWW1</dbase>
			<username>fgwoa</username>
			<password>fgwoa</password>
			<detail>...</detail>
		</dbItem>
	</root>
	
	
	
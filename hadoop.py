import os

def menu():
  while True:
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                            Hadoop Menu               
                                            -----------
    """)
    os.system('tput setaf 6')
    print("""
                                    Press '1': NameNode Configure
                                    Press '2': DataNode Configure
                                    Press '3': Check Report
                                    Press '0': Exit 

        """)
    os.system('tput setaf 4')
    a=input("\t\t\t\t\t  Enter choice: ")
    a=int(a)
    if a == 1:
      os.system('tput setaf 3')
      ip = os.system("ifconfig eth0")
      print("IP of namenode : {}".format(ip))
      os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
      dir = input("Enter directory name with path: ")
      os.system("mkdir {}".format(dir)) 
      datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
      datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>dfs.name.dir</name>
<value>{dir}</value>
</property> 
</configuration>''')
      datafile1=open("/etc/hadoop/core-site.xml", 'w')
      datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://0.0.0.0:9001</value>
</property> 
</configuration>''')

      os.system("systemctl stop firewalld")
      os.system("systemctl disable firewalld")
      os.system("hadoop namenode -format")
      os.system("hadoop-daemon.sh start namenode;jps")
      print("\n\n--------Namenode Started---------")
      x=input()

    elif a == 2:
      os.system('tput setaf 3')
      NN_IP = input("Enter Namenode IP")
      os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
      datadir = input("Enter directory name with path: ")
      os.system("mkdir {}".format(datadir)) 
      datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
      datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>dfs.data.dir</name>
<value>{datadir}</value>
</property>
</configuration>''')
      datafile1=open("/etc/hadoop/core-site.xml", 'w')
      datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
<!-- Put site-specific property overrides in this file.-->


<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{NN_IP}:9001</value>
</property> 
</configuration>''')

      os.system("systemctl stop firewalld")
      os.system("systemctl disable firewalld")
      os.system("rm -rf {datadir};mkdir {datadir}")
      os.system("hadoop-daemon.sh start datanode;jps")
      print("\n\n--------Datanode Started---------")
      x=input()

    elif a == 3:
      os.system('tput setaf 3')
      os.system('hadoop dfsadmin -report')
      x=input()

    elif a == 0:
      os.system('tput setaf 7')
      exit()

    else:
      print("Wrong Choice")	              
menu()

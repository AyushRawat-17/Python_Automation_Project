
import os

def menu():
    os.system('clear')
    os.system('tput setaf 5')
    print(""" 
                                                        AWS Menu
                                                      -----------  
          """)
    os.system('tput setaf 2')
    print("\t\t\t\t\t         Press '0': AWS Help ")
    os.system('tput setaf 3')
    print("""
                                                 Press '1' : Launch an Instance.
                                                 Press '2' : List the Instances.
                                                 Press '3' : Give the Name of Instance.
                                                 Press '4' : Stop an Instance.
                                                 Press '5' : Start an Instance.
                                                 Press '6' : Terminate an Instance.
                                                
                                                 Press '7' : Create a volume.
                                                 Press '8' : Attach the volume.
                                                 Press '9' : Detach the volume.
                                                 Press '10': Delete a volume.

                                                 Press '11': Create S3 bucket.
                                                 Press '12': List the S3 buckets.
                                                 Press '13': Upload in the S3 buckets.
                                                 Press '14': Delete files inside the S3 buckets.
                                                 Press '15': Delete S3 bucket.

                                                 Press '16': Create CloudFront Distribution.
                                                 Press '17': Describe CloudFront Distribution.
                                                 Press '18': Delete CloudFront Distribution.

                                                 Press '99': Write Custom Commands.
                                                 Press '123': Exit.
    """)

while True:
    menu()
    os.system('tput setaf 4')
    cmd = int(input("                                                  Enter Your choice : "))
    if cmd == 0:
      print("You want to see AWS Help.")
      os.system("aws help")
    elif cmd == 1:
      print("\nYou want to Launch the Instance.")
      print("\nChoose Instance :- \n\n")
      print("\t\tPress '1' to RedHat 8.")
      print("\t\tPress '2' to Ubuntu Server 20.04.")
      print("\t\tPress '3' to Ubuntu Server 18.04.")
      print("\t\tPress '4' to Amazon Linux.")
      print("\t\t*Note: Currently not supporting windows.")
      OSchoice = int(input("\n\nEnter Instance of your choice : "))
      if OSchoice == 1:
       os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1  --key-name webserver")
      elif OSchoice == 2:
       os.system("aws ec2 run-instances --image-id ami-0cda377a1b884a1bc --instance-type t2.micro --count 1  --key-name webserver")
      elif OSchoice == 3:
       os.system("aws ec2 run-instances --image-id ami-03f0fd1a2ba530e75 --instance-type t2.micro --count 1  --key-name webserver")
      elif OSchoice == 4:
       os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1  --key-name webserver")
      else:
       print("Your Choice Didnt Match. Sorry!!")
       print("\n\n\t\tInstance Launched.......")		

    elif cmd == 2:
      print("\nYou want to see List of Instances.")
      os.system("aws ec2 describe-instances")

    elif cmd == 3:
      print("\nYou want to Give Name of the Instances.")
      instId1 = input("Enter the Instance-id : ")
      instName = input("Give the Instance-Name : ")
      os.system("aws ec2 create-tags --resource {} --tags Key=Name,Value={}".format(instId1,instName))
      print("\n\n\t\tInstance Name changed.......")

    elif cmd == 4:
      print("\nYou want to stop an Instance.")
      instId2 = input("Enter the Instance-id to stop : ")
      os.system("aws ec2 stop-instances --instance-id {}".format(instId2))
      print("\n\n\t\tInstance Stopped.......")

    elif cmd == 5:
      print("\nYou want to start an Instance.")
      instId3 = input("Enter the Instance-id to start : ")
      os.system("aws ec2 start-instances --instance-id {}".format(instId3))
      print("\n\n\t\tInstance Restarted.......")

    elif cmd == 6:
      print("\nYou want to Terminate an Instance.")
      instId4 = input("Enter the Instance-id to Terminate : ")
      os.system("aws ec2 terminate-instances --instance-id {}".format(instId4))
      print("\n\n\t\tInstance Terminated.......")

    elif cmd == 7:
      print("\nYou want to Create a Volume.")
      az1 = input("Enter the availability-zone : ")
      size = input("Enter the size of volume : ")
      os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az1,size))
      print("\n\n\t\tVolume Created.......")

    elif cmd == 8:
      print("\nYou want to Attach a Volume.")
      volId1 = input("Enter the Volume-id : ")
      instId5 = input("Enter the Instance-id : ")
      os.system("aws ec2 attach-volume --volume-id {} --instance-id  {} --device /dev/sdf".format(volId1,instId5))
      print("\n\n\t\tVolume Attached.......")

    elif cmd == 9:
      print("\nYou want to Detach a Volume.")
      volId2 = input("Enter the Volume-id : ")
      instId6 = input("Enter the Instance-id : ")
      os.system("aws ec2 detach-volume --volume-id {} --instance-id  {} --device /dev/sdf".format(volId2,instId6))
      print("\n\n\t\tVolume Detached.......")

    elif cmd == 10:
      print("\nYou want to Delete a Volume.")
      volId3 = input("Enter the Volume-id : ")
      os.system("aws ec2 delete-volume --volume-id {}".format(volId3))
      print("\n\n\t\tVolume Deleted.......")

    elif cmd == 11:
      print("\nYou want to Create S3 Bucket.")
      bucket1 = input("Enter the Bucket Name : ")
      os.system("aws s3 mb s3://{}".format(bucket1))
      print("\n\n\t\tBucket Created.......")

    elif cmd == 12:
      print("\nYou want to List S3 Bucket.")
      os.system("aws s3 ls")
      print("\n\n\t\tBucket Listed.......")

    elif cmd == 13:
      print("\nYou want to Upload in the S3 Bucket.")
      filepath = input("Enter file with entire filepath :")
      bucket2 = input("Enter the Bucket Name : ")
      os.system("aws s3 cp {} s3://{} --acl public-read".format(filepath,bucket2))
      print("\n\n\t\tFile Uploaded.......")

    elif cmd == 14:
      print("\nYou want to Delete files inside the S3 Bucket.")
      bucket3 = input("Enter the Bucket Name : ")
      os.system("aws s3 rm s3://{} --recursive".format(bucket3))
      print("\n\n\t\tFile Deleted.......")

    elif cmd == 15:
      print("\nYou want to Delete S3 Bucket.")
      bucket4 = input("Enter the Bucket Name : ")
      os.system("aws s3 rb s3://{} --force".format(bucket4))
      print("\n\n\t\tS3 Bucket Deleted.......")

    elif cmd == 16:
      print("\nYou want to Create CloudFront Distribution.")
      dist1 = input("Enter S3 Bucket Name (e.g. : awsexamplebucket.s3.amazonaws.com) : ")
      filename1 = input("Enter Default file-name : ")
      os.system("aws cloudfront create-distribution --origin-domain-name {} --default-root-object {} ".format(dist1,filename1))
      print("\n\n\t\tBucket Created.......")

    elif cmd == 17:
      print("\nYou want to Describe CloudFront Distribution.")
      dist3 = input("Enter Distribution-id : ")
      os.system("aws cloudfront get-distribution --id {}".format(dist3))
      print("\n\n\t\tBucket Described.......")

    elif cmd == 18:
      print("\nYou want to Delete CloudFront Distribution.")
      print("\t\t\n\n***Warning : You have to disable the Distribution Manually..\n\n")
      dist2 = input("Enter Distribution-id : ")
      etag1 = input("Enter Etag : ")
      os.system("aws cloudfront delete-distribution --id {} --if-match {}".format(dist2,etag1))
      print("\n\n\t\tBucket Deleted.......")

    elif cmd == 99:
      print("\nProvide Your Custom Commands.\n")
      cmd12 = input("Enter Your Desired command : ")
      os.system(cmd12)
      print("\n\n\t\tCommand Executed.......")

    elif cmd == 123:
      print("\n\n\t\tExiting...............")
      os.system('tput setaf 7')
      exit()
    else:
      print("You Entered Wrong.")
      print("Press '123' to Delete a volume.")

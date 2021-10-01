import os
import sys
import mimetypes
from email import policy
from email.parser import BytesParser
from fpdf import FPDF 

output_count = 0
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
od=__location__+'/attach'
oPdf=__location__+'/pdf'
os.path.exists(od) or os.makedirs(od)
os.path.exists(oPdf) or os.makedirs(oPdf)
with open(__location__+'/mail.eml', 'rb') as fp:
    msg = BytesParser(policy=policy.default).parse(fp)


f = open("mail.txt", 'a')

print('To:', msg['to'], file=f)
print('From:', msg['from'], file=f)
print('Subject:', msg['subject'], file=f)
simpleBody = msg.get_body(preferencelist=('plain', 'html'))

print(file=f)

print(''.join(simpleBody.get_content().splitlines(keepends=True)), file=f)

print('Attachments:\n')
for attachment in msg.iter_attachments():
    output_filename = attachment.get_filename()
    if output_filename:
        output_count += 1
        print('Attachment {}: {}'.format(output_count,output_filename), file=f)
        with open(os.path.join(od, output_filename), 'wb') as of:
            of.write(attachment.get_payload(decode=True))
    if output_count == 0:
        print("No attachment found", file=f)
pdf = FPDF() 
  
pdf.add_page() 
 
pdf.set_font("Arial", size = 25) 
 
# create a cell 
file = open("mail.txt", "r") 
   
# insert the texts in pdf 
for g in file: 
    pdf.cell(200, 10, txt = g, ln = 1, align = 'C') 
    
 
pdf.output("email.pdf") 

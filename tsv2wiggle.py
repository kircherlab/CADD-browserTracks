import sys

oldpos=0
pos='0'
score=0
for line in sys.stdin:
    if line.startswith('#'):
        continue
    fields = line.strip().split('\t')
    if pos == fields[1]:
        score = max(score, float(fields[5]))
        continue
    
    if int(pos) != oldpos + 1:
        sys.stdout.write('fixedStep chrom=chr%s start=%s step=1 span=1\n' % (fields[0], pos, ))
    sys.stdout.write(str(score) +'\n')    
    
    score = float(fields[5])
    oldpos = int(pos)
    pos = fields[1]
sys.stdout.write(str(score) +'\n')
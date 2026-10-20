const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const path=require('node:path'),root=path.join(__dirname,'..'),read=f=>JSON.parse(fs.readFileSync(path.join(root,f),'utf8'));
const d=read('data.json'),essays=read('essays.json'),E=require('../engine');
assert.equal(d.title,'Research Methodology in SLP');assert.equal(d.lectures.length,9);assert.equal(d.questions.length,930);assert.equal(d.concepts.length,295);assert.equal(essays.length,9);
const ids=new Set(d.questions.map(q=>q.id)),concepts=new Set(d.concepts.map(c=>c.id));assert.equal(ids.size,930);
for(const q of d.questions){assert.equal(q.options.length,4);assert.equal(new Set(q.options).size,4);assert(q.answer>=0&&q.answer<4);assert(q.explanation.length>100);assert(q.sourceIds.length);if(q.conceptId)assert(concepts.has(q.conceptId));}
for(const l of d.lectures){const qs=d.questions.filter(q=>q.lecture===l.id);assert.equal(qs.length,l.count);for(const level of ['Easy','Moderate','Challenging'])assert(qs.some(q=>q.difficulty===level));assert.equal(d.concepts.filter(c=>c.lecture===l.id).length,l.concepts);}
for(const e of essays){assert(e.sections.length>=4);assert(e.sections.flatMap(s=>s.paragraphs).join(' ').split(/\s+/).length>=600);}
for(const size of [10,20,50,100])for(let n=0;n<=1200;n++){const p=E.pages(n,size);assert.equal(p.reduce((a,x)=>a+x.end-x.start,0),n);p.forEach((x,i)=>{assert(x.end-x.start<=size);assert.equal(x.start,i*size);});}
let r=E.record(null,d.questions[0],(d.questions[0].answer+1)%4);assert(r.needsReview);r=E.record(r,d.questions[0],d.questions[0].answer);assert(!r.needsReview&&r.everWrong&&r.attempts===2);
const ctx={window:{}};vm.createContext(ctx);vm.runInContext(fs.readFileSync(path.join(root,'data.js'),'utf8'),ctx);assert.deepEqual(JSON.parse(JSON.stringify(ctx.window.COURSE)),d);
const positions=[0,0,0,0];d.questions.forEach(q=>positions[q.answer]++);assert(positions.every(n=>n>180));
console.log('PASS: 930 unique MCQs, four unique options, correct-index integrity, 295 linked concepts, nine module counts, difficulty coverage, nine substantial essays, data parity, progress logic, pagination and shuffled answer distribution:',positions);

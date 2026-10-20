"""Parse the supplied review; combine it with the authored study key and outlines."""
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'Resources/midterm-review.txt').read_text()
mc, written=text.split('Domain 1: E-Business Infrastructure & Web Fundamentals\nArchitectural Trade-offs:',1)
pattern=r'([^\n]+)\n\nA\) (.*?)\n\nB\) (.*?)\n\nC\) (.*?)\n\nD\) ([^\n]+)'
rows=re.findall(pattern,mc,re.S)
# Restrict each stem to its final nonempty line (excluding Canvas/domain headings).
rows=[(r[0].strip().splitlines()[-1],*r[1:]) for r in rows]
# Keys follow original A–D choice order; instructor answer key was not supplied.
keys=[['B','B','C','B','C','B','A','B','B','B','B','C','B','A','B','B','B','B','A','B'],
['B','A','B','B','B','A','A','A','B','A','B','A','B','A','A','B','A','A','A','A'],
['B','A','B','B','B','B','A','A','A','A','A','A','A','A','B','A','A','A','A','A'],['A']*20,['A']*20]
explanations='''DNS resolves a host name to records such as an IP address so a browser can locate the host. It does not encrypt application data.
A CNAME makes one DNS name an alias of another name. An A record instead contains an IPv4 address.
The client presents the interface and sends requests. The server handles trusted backend processing and database access.
AI can create a starting implementation quickly. Developers still need to inspect, test, and refine its output.
HTTP defines web requests and responses. HTTPS carries HTTP over TLS for protected transport.
An A record associates a DNS name with an IPv4 address. AAAA is the corresponding record type for IPv6.
A headless CMS separates content management from the presentation layer and delivers content through APIs. It may still include an administrative editing interface.
Separate configuration keeps secrets out of committed source and permits different settings for development and production. Environment variables exposed to browser bundles are still public.
A Content Delivery Network caches and serves content from distributed locations, often reducing delivery latency and origin load.
A browser request followed by a server response is a request-response exchange. The response may contain HTML, JSON, or another representation.
An API supplies a defined contract for software interaction. Secure use still requires appropriate authentication, authorization, and validation.
HTTPS uses TLS to encrypt transport and authenticate the server through certificates. SSL is an older, obsolete predecessor.
Git-connected deployments can build and publish updates automatically. Developers remain responsible for security and configuration.
An SPA updates its interface in the browser and commonly fetches data without downloading a complete page on each navigation.
A webhook delivers an event notification to a configured HTTP endpoint. Receivers should authenticate notifications and handle retries safely.
PCI DSS addresses protection of payment card account data. It is distinct from accessibility standards such as WCAG.
Elastic infrastructure adjusts allocated capacity to demand, rather than requiring a permanently fixed allocation.
package.json describes a Node.js package, including its metadata, dependencies, and runnable scripts.
A certificate binds an identity such as a domain to a public key. TLS uses certificates for authentication and negotiates keys to encrypt the connection; a certificate alone does not encrypt traffic.
Promises represent eventual completion or failure. Async/await provides syntax for working with those promises.
Semantic elements convey structure and purpose beyond appearance. Generic div elements do not provide these meanings by default.
WCAG means Web Content Accessibility Guidelines, a set of success criteria for accessible web content.
AA is a common accessibility target and includes all applicable Level A and Level AA criteria. It does not imply every AAA criterion is met.
Without useful alternative text, an image may be announced as a filename or provide no meaningful information. Decorative images should use an empty alt attribute.
Text-to-design tools turn a natural-language brief into an initial interface or component layout that still requires review.
Flexible layout systems and relative sizing let content adapt to available space. Fixed widths alone often produce overflow.
Generated code can contain inaccessible controls, weak semantics, or unnecessary styling. Manual inspection and functional testing are still needed.
A visible label associated using for and id supplies an accessible name. aria-label can provide a name when a suitable visible label is unavailable.
The box model proceeds outward from content to padding, border, then margin. Padding is inside the border; margin is outside it.
Universal Design seeks broad usability from the outset instead of relying on separate adaptations for every user group.
Sufficient contrast makes foreground text distinguishable from its background. Color alone should not carry essential information.
Keyboard testing checks whether users can reach and operate controls without a pointing device, with a visible focus indicator and no keyboard traps.
The main element identifies the dominant content of the page. The pasted question lost this tag; the study app restores it.
Flexbox arranges items along a primary axis, making it well suited to a row or column.
Grid coordinates rows and columns together, making it suited to two-dimensional page layouts.
Relative units and clamp() can adjust text sizing across viewports while respecting usable bounds and user settings.
A transparency log records how AI assistance was used and how a person checked or changed the result. It supports traceability of engineering decisions.
Descriptive link text communicates the destination or action, including when screen reader users browse links out of surrounding context.
Heading levels h1 through h6 express a content hierarchy. Choose levels for structure and style them separately with CSS.
Progressive enhancement begins with a useful baseline, then adds features where supported so core access remains broadly available.
The DOM exposes the document as a tree of nodes that scripts can inspect and update.
An event listener registers a callback for an event. When that event is dispatched, the registered handler can respond.
Developer tools reveal document structure, network traffic, logs, and performance information needed to investigate behavior.
Scope determines where a binding is accessible. Block, function, and module/global scope affect visibility.
let and const are block-scoped; var is function-scoped or global-scoped. const prevents reassignment of the binding but does not make an object immutable.
Unhandled errors and promise rejections commonly produce console diagnostics and stack traces. Their exact display depends on the browser.
JSON is JavaScript Object Notation, a text format for exchanging structured data. It is not executable JavaScript code.
A user controls their browser and can bypass local checks or send requests directly. The server must validate input and enforce authorization.
map returns mapped values, filter selects elements, and reduce accumulates a result. Their callbacks can still mutate referenced objects, so immutability is a coding practice rather than an automatic guarantee.
Controlled fault injection exercises error handling and recovery. It should have defined scope and safeguards.
Client-side routing responds to navigation by updating view state and the DOM, often using the History API.
A runtime error can interrupt the affected execution path and leave the UI incomplete or inconsistent. It does not necessarily freeze the entire browser.
fetch sends asynchronous HTTP requests and returns a Promise for a Response. HTTP error statuses such as 404 normally require checking response.ok.
TypeScript checks declared types before execution. Its types are erased and do not replace runtime validation of external data.
Arrow functions use => and capture this lexically. They differ from ordinary functions in more than spelling.
localStorage persists string key-value data for an origin until cleared. It is accessible to page scripts and unsuitable for sensitive secrets.
try/catch handles exceptions in its protected execution. To catch a rejected Promise this way, await it inside the try block or attach an appropriate rejection handler.
DOM manipulation changes document nodes or their attributes, allowing interfaces to react without a complete page reload.
A stack trace identifies the chain of calls and source locations associated with an error, helping locate its cause.
A closure retains access to the lexical bindings around a function, even after the outer call has returned.
PostgreSQL is an open-source object-relational database system. It stores and queries structured data and supports transactions and constraints.
CRUD groups four basic data operations: Create, Read, Update, and Delete.
Row-Level Security policies control which rows are accessible for operations. Authentication and correct policy configuration are still needed; privileged roles can bypass RLS in some cases.
SQL injection occurs when untrusted input changes a query's executable structure, potentially exposing or modifying data.
Bound parameters keep values separate from SQL structure. ORMs protect parameterized operations, but unsafe raw SQL or string concatenation can still introduce injection.
Express supplies routing and middleware on top of Node.js HTTP functionality. It is not a database or a frontend component library.
A schema defines how data is organized: tables, columns, types, relationships, and constraints.
Backend environment configuration separates deployment values and secrets from tracked application code. Never commit real secrets or ship them in frontend bundles.
Authentication verifies identity using credentials or tokens. The intended answer is A, but authorization is the separate check of what that identity may do.
A foreign key references a primary or other unique key to enforce relationships. Foreign key values may repeat in the referencing table, as in many orders belonging to one customer.
Middleware functions participate in the request-response cycle. They can inspect or change requests, send a response, or pass control onward.
Indexes help locate rows efficiently, at the cost of storage and maintenance during writes. Their benefit depends on the query and data.
POST typically submits data for processing or creates a resource. It is not inherently idempotent.
GET retrieves a representation and is defined to have safe semantics. It should not be used for requested state-changing operations.
TLS protects credentials in transit against passive interception and helps authenticate the server. It does not secure compromised endpoints.
Normalization organizes related facts to reduce duplication and update anomalies while preserving data integrity.
A primary key uniquely identifies each row and is non-null. It may consist of one column or several columns.
Rate limits cap requests within a window to reduce abuse and overload. They are one layer of defense and do not stop every denial-of-service attack.
An API endpoint is an address at which a service exposes an operation or resource, commonly combined with an HTTP method.
Atomicity makes a transaction all-or-nothing. For example, an order insertion and inventory update can commit together or roll back together.
Git tracks versions as a distributed repository, supporting local history and collaborative branching and merging.
A commit records a repository snapshot plus metadata, including a message and links to its parent commits.
Branches provide separate lines of development so changes can be prepared and reviewed before integration.
A pull request proposes integrating changes and provides a place for discussion, review, and automated checks.
.gitignore excludes matching untracked files from normal tracking. It does not remove secrets or files already committed; leaked secrets must be rotated.
CI runs automated verification when changes are integrated or proposed. It can include builds, tests, and static analysis.
Small focused commits with descriptive messages explain intent and make review, debugging, and reverting easier.
Code review lets peers inspect correctness, security, maintainability, and consistency while sharing knowledge.
A README gives collaborators an entry point for understanding, setting up, and using a project.
Release management coordinates how tested changes are packaged, scheduled, deployed, and maintained in production.
The supplied review describes the capstone as an end-to-end demonstration of full-stack business application skills. Use the actual assignment rubric for grading requirements.
Linting checks source for likely problems and conventions; formatting tools such as Prettier focus on consistent presentation. The intended combined choice is A.
An issue tracker records work items, ownership, priorities, and status through the project lifecycle.
Traceable contributions and reviews help teams distribute work fairly and demonstrate individual participation.
A Git tag gives a stable name to a particular object, usually a commit marking a release milestone.
The supplied review frames the defense and reflection around technical choices, a working demonstration, and lessons from AI-assisted development.
Workflow hygiene includes clear organization, readable history, useful branch names, and keeping credentials out of version control.
Automated tests check expected behavior repeatedly and detect regressions. Test quality and coverage determine which problems they can catch.
Documentation explains how the system is structured, used, deployed, and maintained so future contributors can work effectively.
Incremental delivery exposes risks earlier and enables feedback and verification throughout development, reducing last-minute integration surprises.'''.splitlines()
topics=[
['DNS','DNS','Client-server architecture','AI collaboration','HTTP & TLS','DNS','Content architecture','Configuration & secrets','Content delivery','HTTP & TLS','APIs & events','HTTP & TLS','Deployment & scaling','Client-server architecture','APIs & events','Payment security','Deployment & scaling','Project configuration','HTTP & TLS','Async JavaScript'],
['Semantic HTML','Accessibility fundamentals','Accessibility fundamentals','Accessible images','AI UI scaffolding','Responsive layout','AI UI scaffolding','Accessible forms','CSS fundamentals','Accessibility fundamentals','Color contrast','Keyboard access','Semantic HTML','Responsive layout','Responsive layout','Responsive typography','AI transparency','Accessible links','Semantic HTML','Progressive enhancement'],
['DOM & events','DOM & events','Debugging','Scope & closures','Scope & closures','Debugging','JSON & APIs','Input validation','Array transformations','Debugging','SPA navigation','Debugging','JSON & APIs','TypeScript','JavaScript syntax','Browser storage','Error handling','DOM & events','Debugging','Scope & closures'],
['Relational databases','CRUD & HTTP methods','Database security','SQL injection','SQL injection','Routing & middleware','Schema & constraints','Configuration & secrets','Authentication & authorization','Schema & constraints','Routing & middleware','Database indexing','CRUD & HTTP methods','CRUD & HTTP methods','Transport security','Normalization','Schema & constraints','API security','API endpoints','Transactions'],
['Git fundamentals','Git fundamentals','Branches & pull requests','Branches & pull requests','Repository hygiene','Continuous integration','Commits & reviews','Commits & reviews','Documentation','Release management','Capstone governance','Code quality','Project management','Team accountability','Release management','Capstone governance','Repository hygiene','Automated testing','Documentation','Iterative delivery']]
assert len(rows)==len(explanations)==100,(len(rows),len(explanations))
bank=[]
for i,(stem,*options) in enumerate(rows):
    if i==20: stem='Why is the use of semantic HTML5 elements (such as <header>, <nav>, <main>, and <footer>) preferred over generic wrappers?'
    if i==27: options[0]='aria-label or associated <label> elements with matching for and id attributes'
    if i==32: stem='What is the function of the <main> landmark element in semantic HTML?'
    if i==38: stem='What is the purpose of semantic heading tags (<h1> through <h6>)?'
    bank.append(dict(id=f'Q{i+1:03}',chapter=i//20+1,number=i+1,topic=topics[i//20][i%20],difficulty='Review',statement=stem,options=options,answer=keys[i//20][i%20],explanation=explanations[i],sources=[{'file':'midterm-review.txt','location':f'Question {i+1}'}]))
(ROOT/'question-bank.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
written='Architectural Trade-offs:'+written
sections=re.split(r'\n\nDomain \d: [^\n]+\n',written)
assert len(sections)==5
outlines=json.loads((ROOT/'tools/essay-outlines.json').read_text())
essays=[]
for domain,section in enumerate(sections,1):
    for item in section.strip().split('\n\n'):
        title,prompt=item.strip().split(': ',1)
        n=len(essays)
        essays.append(dict(id=f'E{n+1:02}',chapter=domain,title=title,prompt=prompt,points=outlines[n]['points'],example=outlines[n]['example']))
assert len(essays)==10
(ROOT/'essay-bank.json').write_text(json.dumps(essays,ensure_ascii=False,indent=2)+'\n')
print(f'Built {len(bank)} multiple-choice questions and {len(essays)} written prompts.')

<%inherit file="/base.mako" />

<h2>Your reviews</h2>

<table>
<tr>
<th>Proposal title</th>
<th>Score</th>
<th>Stream</th>
<th>Comment</th>
<th>Edit</th>
</tr>
% for r in c.review_collection:
%	if r.reviewer == h.signed_in_person():

<tr class="${ h.cycle('even', 'odd') }">

<td>
${ h.link_to("%s - %s" % (r.proposal.id, r.proposal.title), url=h.url_for(controller='review', action='edit', id=r.id)) }
</td>

<td>
${ r.score |h }
</td>

<td>
% if r.stream is not None:
${ r.stream.name |h }
% else:
(none)
% endif
</td>

<td>
${ h.truncate(r.comment) }
</td>

<td>
${ h.link_to("edit", url=h.url_for(controller='review', action='edit', id=r.id)) }&nbsp;-&nbsp;${ h.link_to("delete", url=h.url_for(controller='review', action='delete', id=r.id)) }
</td>
</tr>

% 	endif
% endfor
</table>

<%def name="title()" >
Reviews - ${ parent.title() }
</%def>


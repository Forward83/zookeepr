<%inherit file="/base.mako" />

<h2>Coming soon!</h2>

<p>
The call for presentations has not opened yet. Please visit back later.
</p>

<p>
Return to the <a href="${ h.url_for("home") }">main page</a>.
</p>

<%def name="title()" >
Call for Presentations - coming soon - ${ caller.title() }
</%def>

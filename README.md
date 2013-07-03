<h1>DOT-Data-Feeds</h1>
<p>
"The Department of Transportation (DOT) provides numerous data feeds including Traffic Advisories, Street Construction worksites, bicycle parking and cycling map, as well as information regarding the Staten Island Ferry, alternate side parking and parking regulations, Citywide Low Bridges, New York City Truck Routes, and Street Network Changes.  DOT also provides real time data from traffic cameras and traffic speed detectors.  Note that these data feeds may contain and/or utilize information which was originally compiled by the New York City Department of Transportation (DOT) for governmental purposes; the information may subsequently been modified by entity/entities other than DOT. DOT and the City of New York make no representation as to the accuracy or usefulness of the information provided by this application or the information's suitability for any purpose and disclaim any liability for omissions or errors that may be contained therein. The public is advised to observe posted signage for compliance with applicable laws and regulations.
</p>


<b>To use the included Python Library, you must first import it:</b><br />
<code>import DOT</code>

If the library fails to import, make sure python is set to search the directory that the file is located in. Then restart python and try again.



<b>Creating a DOT object and setting the API Key/ID:</b><br />
<code>myobj = DOT.DOT('API ID' , 'API Key') </code>


<b>Changing the API Key or ID for a DOT object that was already created: </b><br />
<code>
myobj.setID('NewID')<br />
myobj.setKey('NewKey')
</code>


<b>Getting the API Key or ID for a DOT object that was already created: </b><br />
<code>
myobj.getID() <br />
myobj.getKey()
</code>


<b> Using an already created object, search for "Weekly Traffic Info"</b><br />
<code>
myobj.getTrafficInfo(myobj.t_WeeklyTraf)
</code>



<b>For DOT Truck info and Bike info, you can select whether to have your result returned as a ZIP or a KML: </b>
<code>
myobj.getTruckInfo(myobj.r_AllRoutes , myobj.kml)</code><br />
<b>OR</b><br />
<code>
myobj.getTruckInfo(myobj.r_AllRoutes , myobj.zip)
</code>

<b>For further documentation and examples, see the integrated help DOC in python:</b><br />
<code>help(DOT) </code>








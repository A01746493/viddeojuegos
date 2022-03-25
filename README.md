
<html><head><title>Python: module Parabolico</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>Parabolico</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:c%3A%5Cusers%5Cdell%5Conedrive%5Cdocumentos%5Cgithub%5Cviddeojuegos%5Cparabolico.py">c:\users\dell\onedrive\documentos\github\viddeojuegos\parabolico.py</a></font></td></tr></table>
    <p><tt>Cannon,&nbsp;hitting&nbsp;targets&nbsp;with&nbsp;projectiles.<br>
&nbsp;<br>
Exercises<br>
&nbsp;<br>
1.&nbsp;Keep&nbsp;score&nbsp;by&nbsp;counting&nbsp;target&nbsp;hits.<br>
2.&nbsp;Vary&nbsp;the&nbsp;effect&nbsp;of&nbsp;gravity.<br>
3.&nbsp;Apply&nbsp;gravity&nbsp;to&nbsp;the&nbsp;targets.<br>
4.&nbsp;Change&nbsp;the&nbsp;speed&nbsp;of&nbsp;the&nbsp;ball.</tt></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-draw"><strong>draw</strong></a>()</dt><dd><tt>Draw&nbsp;ball&nbsp;and&nbsp;targets.</tt></dd></dl>
 <dl><dt><a name="-inside"><strong>inside</strong></a>(xy)</dt><dd><tt>Return&nbsp;True&nbsp;if&nbsp;xy&nbsp;within&nbsp;screen.</tt></dd></dl>
 <dl><dt><a name="-move"><strong>move</strong></a>()</dt><dd><tt>Move&nbsp;ball&nbsp;and&nbsp;targets.</tt></dd></dl>
 <dl><dt><a name="-tap"><strong>tap</strong></a>(x, y)</dt><dd><tt>Respond&nbsp;to&nbsp;screen&nbsp;tap.</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>ball</strong> = vector(-200, -200)<br>
<strong>speed</strong> = vector(0, 0)<br>
<strong>targets</strong> = [vector(78.0, -128), vector(89.5, -61), vector(120.5, 94), vector(131.5, -126), vector(151.5, 77), vector(156.0, 55), vector(183.0, 92), vector(196.0, -90)]</td></tr></table>
</body></html>

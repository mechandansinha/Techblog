Title: Ask Permission To Save Image | Javascript 
Date: 2016-10-07 10:00 PM
Category: random
Tags: settings, javascript, web
Summary: How to trigger dialog box when someone right clicks on your copyrighted image and tries to save it.

Recently while visiting a [photography blog](http://www.blissfulsnapshots.com/p/blog-page_2.html), I came across an
animated picture and tried to save it. But when I right-clicked on that image, instead of the usual context menu, a dialog box 
popped up which said this -

<center><img src="images/dialog1.png"></img><br></center>

Here's the picture -

<center><img src="https://4.bp.blogspot.com/-ZOGmadkxQbM/VtQGcyfXP1I/AAAAAAAAE9I/S-3rnporv0E/s200/camera1.png"></img><br></center>

I was intrigued by it as I had never come across this feature in my 2 years of web-development experience. I tried to find out how
is it being done by going through the code -

```html
<div class="separator" style="clear: both; text-align: center;">
	<a href="https://4.bp.blogspot.com/-ZOGmadkxQbM/VtQGcyfXP1I/AAAAAAAAE9I/S-3rnporv0E/s1600/camera1.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;">
		<img border="0" height="200" src="https://4.bp.blogspot.com/-ZOGmadkxQbM/VtQGcyfXP1I/AAAAAAAAE9I/S-3rnporv0E/s200/camera1.png" width="200">
	</a>
</div>
``` 
But as you can see, there wasn't any apparent javascript code associated with it that might have triggered that. Anyway I was
able to get the image by copying the URL (as you can see above) but I probed in little further.

As you can see there isn't any special class associated with ``` <div>, <a> or <img> ``` tags except ```.separator``` which is there with every element in the hierarchy (not shown here). It isn't doing anything specific here. Since the case is only with the images, there must be something with ``` <img> ``` itself.

Initially I searched about it on Google but I could find relevant stuffs given the ambigous formulation of the query. Anyway I carefully went through the javascript code one by one. It's error-prone to do right in <i> ```Element``` </i> section -

```javascript
	  //<![CDATA[
	  	$("#LinkList60").each(function(){$(this).addClass('main-menu');var e="<ul id='nav'><li><ul class='sub-menu'>";
		$("#LinkList60 li").each(function(){var t=$(this).text(),n=t.substr(0,1),r=t.substr(1);"_"==n?(n=$(this).find("a").attr("href"),e+='<li><a href="'+n+'">'+r+"</a></li>"):(n=$(this).find("a").attr("href"),e+='</ul></li><li><a href="'+n+'">'+t+"</a><ul class='sub-menu'>")});e+="</ul></li></ul>";$(this).html(e);
		$("#LinkList60 ul").each(function(){var e=$(this);if(e.html().replace(/\s|&nbsp;/g,"").length==0)e.remove()});
		$("#LinkList60 li").each(function(){var e=$(this);if(e.html().replace(/\s|&nbsp;/g,"").length==0)e.remove()});
		$('#LinkList60 a').each(function(){var page_url=$(location).attr('href'),link=$(this).attr('href');if(link===page_url){var id=$(this).parents(':eq(1)').attr('id');if(id==='nav'){$(this).parent('li').addClass('current')}else{$(this).parents(':eq(2)').addClass('current')}}});
		$('.sub-menu').prev('a').append("<i class='fa fa-angle-down'/>");selectnav('nav')});
	      //]]>  
```
There I found that this site uses lot of custom javasript -

```javascript

  //<![CDATA[
  /*
By Osvaldas Valutis, www.osvaldas.info
Available for use under the MIT License
*/
  (function(e,t,n,r){e.fn.doubleTapToGo=function(r){if(!("ontouchstart"in t)&&!navigator.msMaxTouchPoints&&!navigator.userAgent.toLowerCase().match(/windows phone os 7/i))return false;this.each(function(){var t=false;e(this).on("click",function(n){var r=e(this);if(r[0]!=t[0]){n.preventDefault();t=r}});e(n).on("click touchstart MSPointerDown",function(n){var r=true,i=e(n.target).parents();for(var s=0;s<i.length;s++)if(i[s]==t[0])r=false;if(r)t=false})});return this}})(jQuery,window,document);
  //]]> 

```
After fumbling a bit more, I found this in <i> Application </i> section of the debugger (under **Frames**) -

```javascript

    //<![CDATA[
    /* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Disable context menu on images by GreenLava (BloggerSentral.com)
Version 1.0
You are free to copy and share this code but please do not remove this credit notice.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ */
    function nocontext(e) {
      var clickedTag = (e==null) ? event.srcElement.tagName : e.target.tagName;
      if (clickedTag == "IMG") {
        alert(alertMsg);
        return false;
      }
    }
    var alertMsg = "Please ask permission if you want to use my photos. Thank you! :)";
    document.oncontextmenu = nocontext;
    //]]>

```
This script was triggering the dialog-box. It disables the context menu specifically on images. it uses ```.oncontextmenu``` method of ```document``` object and sets it to ``` nocontext ```. 

I've utilized the same here. If you try to save any of the images, it will trigger the same dialog box (with edited message ofcourse :P)

It's a nice way to protect your images on the website (atleast one layer of friction). Also the person would be notified that you need to seek permission. 

Hope you learnt something new today. Keep experimenting. Peace out ✌

<script type="text/javascript">

 //<![CDATA[
    /* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Disable context menu on images by GreenLava (BloggerSentral.com)
Version 1.0
You are free to copy and share this code but please do not remove this credit notice.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ */
    function nocontext(e) {
      var clickedTag = (e==null) ? event.srcElement.tagName : e.target.tagName;
      if (clickedTag == "IMG") {
        alert(alertMsg);
        return false;
      }
    }
    var alertMsg = "Thanks for testing this feature! Keep visiting :)";
    document.oncontextmenu = nocontext;
    //]]>

</script>

---
title: "bing - Microsoft Search Engine"
date: 2009-06-12T11:29:23+09:00
tags: ['Archived']
---

ようやく bing にこのサイトが掲載されました。<br/>
<br/>
クローラーが毎日検索していたことを考えると、サイトの存在性のチェック、更新頻度のチェック、外部リンクのチェックなどを行い、期間と基準を満たしたときに掲載されるのでしょう。<br/>
<br/>
サイト登録をしてからちょうど1週間で掲載です。<br/>
<br/>
<strong>robots.txt</strong>
<code style="display:block;background-color:#cccccc;padding:3px;">
User-agent: *<br/>
SiteMap: http://your_site_URL/sitemap.xml<br/>
Disallow:<br/>
</code>
<br/>
<strong>sitemap.xml (UTF-8)</strong><br/>
<code style="display:block;background-color:#cccccc;padding:3px;">
&lt;?xml version="1.0" encoding="UTF-8"?&gt;<br/>
&lt;urlset<br/>
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"<br/>
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"<br/>
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9<br/>
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"&gt;<br/>
&lt;!-- created with Free Online Sitemap Generator www.xml-sitemaps.com --&gt;<br/>
<br/>
&lt;url&gt;<br/>
  &lt;loc&gt;http://your_site_URL/&lt;/loc&gt;<br/>
  &lt;priority&gt;1.00&lt;/priority&gt;<br/>
  &lt;lastmod&gt;2009-06-05T00:51:04+00:00&lt;/lastmod&gt;<br/>
  &lt;changefreq&gt;hourly&lt;/changefreq&gt;<br/>
&lt;/url&gt;<br/>
&lt;url&gt;<br/>
 :<br/>
 :<br/>
&lt;/url&gt;<br/>
&lt;/urlset&gt;<br/>
</code>
<br/>
<br/>
設置した robots.txt と sitemap.xml のサンプルです。<br/>
登録した後は我慢して待つのみ。<br/>
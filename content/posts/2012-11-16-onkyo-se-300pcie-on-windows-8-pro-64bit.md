---
title: "ONKYO SE-300PCIE on Windows 8 Pro 64bit"
date: 2012-11-16T15:02:17+09:00
draft: false
categories: ['AUDIO', 'COMPUTER']
tags: []
---

&nbsp;

ONKYO SE-200PCI LTD が、OSやドライバーの構成状況、インストールタイミングによって、PCIバスでの信号遅延が発生し、音飛びやノイズが発生していた状態だったので、辛抱たまらず、<a href="http://www.jp.onkyo.com/pcaudio/pciedigitalaudioboard/special/" target="_blank">ONKYO SE-300PCIE</a> に買い換えました。

商品名にもあるとおりPCI-Enhanced バスを使用します。

SE-300PCIE はカードの高さがあり、隣のバスに干渉しますので2スロット分の空きが必要になります。

GIGA-BYTE GA-990FXA-UD3の一番下のスロットに差し込んでやろうとしたら、USB2.0やUSB3.0、IEEE1394のコネクタに干渉して取り付けできませんでした。

下から2番目のスロットはPCIなので、ここにはSE-300PCIEの拡張コネクタを差し込みます。

下から3番目のスロットのPCI-E x16にSE-300PCIEの本体を差し込みました。

グラフィックカードのSLIやCrossFireを使わないなら、ここで問題ないでしょう。

PCI-E x1が2スロットありますが、ことごとくグラフィックカードと干渉します。
<table border="1" cellspacing="0">
<tbody>
<tr>
<th>スロット</th>
<th>差し込みカード</th>
<th>バックパネル</th>
</tr>
<tr>
<td>PCI-E x1-1</td>
<td>空き</td>
<td>空き</td>
</tr>
<tr>
<td>PCI-E x16-1</td>
<td>Radeon HD 5670</td>
<td>Radeon HD 5670</td>
</tr>
<tr>
<td>PCI-E x1-2</td>
<td>空き</td>
<td>空き</td>
</tr>
<tr>
<td>PCI-E x4-1</td>
<td>空き</td>
<td>空き</td>
</tr>
<tr>
<td>PCI-E x16-2</td>
<td>SE-300PCIE</td>
<td>SE-300PCIE</td>
</tr>
<tr>
<td>PCI</td>
<td>空き</td>
<td>SE-300PCIE</td>
</tr>
<tr>
<td>PCI-E x4-2</td>
<td>空き</td>
<td>USB2.0/IEEE1394</td>
</tr>
</tbody>
</table>
こんな感じです。

SE-300PCIE を PCI-E x1 に接続すると認識されないなどの現象があるようです。

x4以上のスロットなら大丈夫らしいです。

PCI-E x4-1のスロットにそのうち差し替えます。

&nbsp;

気になる音質ですが、美辞麗句や酷評は薀蓄を語る人たちに任せます。

最近では「付帯感のない」などという意味のわからない言葉が横行してます。

あげぽよと同じくらい意味わからないです。

結局のところ聞きやすいかどうかだけ。

で、SE-300PCIE は聞きやすい。

もうひとつ、音飛びやノイズがなくなってストレス解消ですわ。

&nbsp;

百万超えの外付けUSB音源で音飛びしているやつとか、もう悲惨としかいえないだろ。

&nbsp;
---
title: "Walkman Application in Sony Xperia Tablet S"
date: 2013-04-08T16:52:47+09:00
draft: false
categories: ['AUDIO', 'COMPUTER']
tags: []
---

Sony Xperia Tablet SにインストールされているWalkmanアプリは、DLNAに<wbr />対応しています。

DLNAサーバー（Windows Media SeverやDLNA対応HDDなど)に蓄積された音楽ファイル<wbr />を再生することができます。

WindowsアプリケーションのFoobar2000のUPn<wbr />Pサーバー機能を使って、再生することができます。
... ただしストリーム形式はmp3じゃないといけません。
ほかのDLNAクライアントと併用する場合は、Foobar20<wbr />00側の設定で、Tablet用のプロファイルを作成します。
Use profile when に「X-AV-Client-Info」を、containに「<wbr />av=5.0; cn="Sony"; mn="SGPT12"; mv="2.0";」を設定します。
Walkmanアプリは、バグがあるというか、DLNA仕様にそ<wbr />ってないのか、Foobar2000とは相性が悪いです。
プレイリストが表示されなかったり、再生できないプレイリストが<wbr />あったり・・・。
Foobar2000のマルチバイト文字列の扱いにバグがあるせ<wbr />いかもしれませんけれど。

<a href="http://qa.support.sony.jp/solution/S1210240043242/?p=&amp;q=DLNA&amp;rt=qasearch&amp;srcpg=tablet">http://qa.support.sony.jp/solution/S1210240043242/?p=&amp;q=DLNA&amp;rt=qasearch&amp;srcpg=tablet</a>
ここにWalkmanアプリのDLNA仕様に正確に対応していないことが書かれています。
シングルクォート「'」が、ファイル名やタイトル、アーティスト名などの文字列に含まれていると再生できないとことです。
B'zの楽曲は無理と言うことに…。
一度再生を失敗した楽曲情報は、Devicesに記録されてしまっているので、これのキャッシュと
データを削除しないと再生できません。
こんなヘルプを書くぐらいなら、改善をしてほしいモノです。

--Add 2013/04/22--

4月18日のアップデートで「'」シングルクォートの問題が改修されています。

そのほかの細かなバグが改修されています。画面がフラッシュしたり、電源が落ちたりすることもなくなっています。

ちなみにFoobar2000のDLNAサーバーのデバッグログをとることで、X-AV-Client-Infoを調べることができます。

--end--

ほかにWalkmanアプリは「Throw」という機能がありま<wbr />す。
DLNA対応でWindows Media Playerのリモート再生に対応した機器(UPnPメディア機<wbr />器)にデータを送信して再生することができます。
データは、画像、音楽、動画などです。
MacでいうところのAirPlayに近いでしょうか。
このThrowを使うと、Walkmanアプリで再生操作すると<wbr />Wi-FiでつながったAVアンプから音が出ます。

私の持っているAVアンプ(DENON AVC-4320)がWindows Media Playerのリモート再生に対応していることを初めて知ったの<wbr />は、購入してから数年たったころでした。
Windows VISTA認証機器ということは知っていたのですが・・・。
マニュアルにも書いてなかったし、Windows Media Playerのヘルプにもそんなことが書いてなかったので判らな<wbr />かったのです。
あるときONKYOの製品紹介ページを見ているときに、Wind<wbr />ows VISTA/<wbr />7認証のAVアンプ製品のことが記述されていたので、同じくWin<wbr />dows VISTA/<wbr />7の認証機器のDENON AVC-4320もできるはずと思って、Windows7からリモート再生した<wbr />らできたのです。

で、今日、WalkmanアプリからThrowをしてみたら、A<wbr />Vアンプから音が出ました。

Android端末でできることが意外に多いです。
ベースになったのはLinuxだから当たり前か…。

しかしDLNAに関しては、知らないことが多すぎます。

Sony Xperia スマートフォンを持っていてWalkmanアプリが使える場合は<wbr />、Throwを試してみたらどうでしょうか。

&nbsp;

Sony Xperia Tablet S のWalkman の Throw機能は、ファイル形式がAAC、mp3、WMAのみに対応しています。

詳しくは以下のURLより

<a href="http://www.sony.jp/support/dlna/lineup.html">http://www.sony.jp/support/dlna/lineup.html</a>
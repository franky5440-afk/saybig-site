#!/usr/bin/env python3
"""Generate the Saybig site (static HTML, no JS). Run: python3 build.py
All page text lives in this file; edit here, then re-run."""
import os

BASE = "https://franky5440-afk.github.io/saybig-site/"
EMAIL = "franky5440@hotmail.com"
UPDATED = "2026-11-20"
VERSION = "1.0"
ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = {
    "en": {
        "lang": "en", "name": "Saybig",
        "title": "Saybig: Speech to Big Text",
        "desc": "Saybig turns what you say into huge text on your iPhone screen so the person across from you can read it. On-device recognition, no account, no data collection.",
        "nav": [("guide", "Guide"), ("support", "Support"), ("privacy", "Privacy")],
        "switch": "中文", "switch_lang": "zh-Hant", "page_titles": {"guide": "User guide", "support": "Support", "privacy": "Privacy policy"},
    },
    "zh": {
        "lang": "zh-Hant", "name": "說給你看",
        "title": "說給你看：講話變大字",
        "desc": "說給你看會把你說的話變成超大的字，讓對面的人直接看手機螢幕。辨識在手機上完成，不用帳號、不收集資料。",
        "nav": [("guide", "使用說明"), ("support", "支援"), ("privacy", "隱私權")],
        "switch": "English", "switch_lang": "en", "page_titles": {"guide": "使用說明", "support": "支援", "privacy": "隱私權政策"},
    },
}

EN = {}
ZH = {}

EN["index"] = """
<h1>Saybig</h1>
<p class="meta">Speech to Big Text for iPhone.</p>
<p>Talk to your iPhone and Saybig turns your words into huge text on the screen, so the person across from you can simply read it. The person reading never has to touch the phone.</p>
<ul>
<li><strong>Talk, and they read.</strong> Your words appear as big, bold text a moment after you say them. Stand the phone up, or turn it around to show them.</li>
<li><strong>Type when talking won't do.</strong> Type a sentence and show it in the same big text. This keeps working after the free trial.</li>
<li><strong>Stays on your phone.</strong> Your voice is recognized on the iPhone itself. It is not uploaded and not saved as a recording. No account, no ads, no data collection.</li>
<li><strong>Made for iPhone Duo too.</strong> Half-open, it stands on the table like a caption card: big text facing them, controls facing you.</li>
</ul>
<p>Good for talking with grandparents, at a clinic counter or pharmacy, with a caregiver, or anywhere it is too noisy to be heard. Speech recognition understands Mandarin (Taiwan) and English. It does not understand Taiwanese Hokkien, and like any speech recognition it will sometimes get a word wrong, so check the small preview on your side.</p>
<p><strong>App Store:</strong> Coming soon. Free download, 7-day free trial, then a one-time US$2.99 unlock. No subscription.</p>
<p><a href="guide/">Read the user guide</a> · <a href="support/">Support</a> · <a href="privacy/">Privacy policy</a></p>
"""

ZH["index"] = """
<h1>說給你看</h1>
<p class="meta">講話變大字，iPhone 上的字幕工具。</p>
<p>對著 iPhone 講話，說給你看會立刻把你的話變成超大的字，讓對面的人直接看螢幕。看字的人完全不用碰手機。</p>
<ul>
<li><strong>你講，他看。</strong>話一說完，大大的粗體字就出現在螢幕上。把手機立起來，或轉過去給對方看都可以。</li>
<li><strong>不方便講話就用打的。</strong>打一句話，用同樣的大字秀出來。試用結束後這個功能照樣能用。</li>
<li><strong>資料留在你的手機。</strong>聲音在 iPhone 上直接辨識，不上傳、不存成錄音。不用帳號、沒有廣告、不收集資料。</li>
<li><strong>iPhone Duo 也好用。</strong>半開立在桌上就像一塊字幕牌：大字面向對方，控制按鈕面向你。</li>
</ul>
<p>適合跟家裡長輩說話、在診所或藥局櫃檯、請看護溝通，或是太吵聽不清楚的地方。語音辨識聽得懂國語（台灣）與英文，聽不懂台語；而且跟所有語音辨識一樣，偶爾會有同音字錯誤，建議看一下自己這邊的小字預覽。</p>
<p><strong>App Store：</strong>即將上架。免費下載、7 天免費試用，之後一次付清 US$2.99 解鎖。沒有訂閱。</p>
<p><a href="guide/">看使用說明</a> · <a href="support/">支援</a> · <a href="privacy/">隱私權政策</a></p>
"""

EN["guide"] = """
<h1>User guide</h1>
<p class="meta">For Saybig 1.0 on iPhone (iOS 26 or later).</p>

<h2>How it works</h2>
<p>The screen has two parts. The <strong>big text area</strong> at the top is for the other person. The <strong>control area</strong> at the bottom, about 30% of the screen, is for you: the microphone button, a small preview of the latest sentence, and four small buttons (Keyboard, Face-to-face, History, Settings), plus <strong>Clear</strong> next to the preview.</p>

<h2>First time</h2>
<ol>
<li>Open Saybig. The first screen reads “Try Saybig free for 7 days”.</li>
<li>Tap <strong>Start 7-Day Free Trial</strong>. It costs nothing. (Or tap <strong>Buy Full Version</strong> to unlock it right away.)</li>
<li>You land on the main screen. It says “Tap the microphone and start talking”.</li>
</ol>

<h2>Talk and show</h2>
<ol>
<li>Tap the microphone button. The first time, iPhone asks to use the microphone. Tap Allow.</li>
<li>The first time you use a language, iPhone downloads its speech recognition data once. You will see “Downloading speech recognition resources (one time only)” with progress. This is the only time Saybig goes online, and iOS does the download. If it fails, tap <strong>Try Again</strong>.</li>
<li>Talk. Your words appear in the big text area. Text that may still change is a little see-through; once it settles it turns solid.</li>
<li>When you pause briefly, or finish a sentence, your next words start on a new line. Older lines dim, and the newest one stays bright.</li>
<li>Tap the microphone button again to pause. Tap it once more to carry on.</li>
</ol>
<p>The small preview in the control area shows your latest sentence so you can check what the other person sees. If you say nothing for 3 minutes, Saybig pauses itself. If you leave the app or a call comes in, it stops listening, and you tap the microphone again to resume. While it listens, the screen does not auto-lock.</p>
<p>Scrolled back to read an earlier sentence? Tap <strong>Jump to latest</strong>, or just leave it for 5 seconds and it jumps back when new words arrive. Tap <strong>Clear</strong> to wipe the big text area and start a new conversation. Your History is not affected.</p>

<h2>Face to face</h2>
<p>When the other person sits across from you, the big text area is turned upside down so it reads correctly from their side. This is on by default. Tap <strong>Face-to-face</strong> to turn it off, for example when you hand the phone over, or when you sit side by side. You can also set it in Settings.</p>

<h2>Type instead of talking</h2>
<ol>
<li>Tap <strong>Keyboard</strong>. A text box appears and the keyboard comes up. Listening pauses.</li>
<li>Type your sentence and tap <strong>Show</strong>. It appears in the big text area. The box clears and the keyboard stays, so you can keep typing.</li>
<li>Tap <strong>Close Keyboard</strong> to go back to the controls.</li>
</ol>
<p>Typing to big text keeps working after the free trial ends.</p>

<h2>History</h2>
<p>Tap <strong>History</strong> to see past sentences, grouped by day, newest first. Typed sentences have a small keyboard icon.</p>
<ul>
<li>Tap a sentence to show it full screen again, in your current text size and colors. Tap once more, or tap Close, to come back.</li>
<li>Swipe left on a sentence to delete it. Tap <strong>Clear All</strong> (and confirm) to delete everything.</li>
<li>History is stored only on your iPhone. Turn off <strong>Save History</strong> in Settings and new sentences are no longer saved.</li>
</ul>
<p>History keeps working after the free trial ends.</p>

<h2>Settings</h2>
<ul>
<li><strong>Full Version</strong>: shows your trial days left, or “Unlocked”, plus Buy and <strong>Restore Purchases</strong>.</li>
<li><strong>Text Size</strong>: five steps, from “10 characters per line” to “5 characters per line”. The default is 7. Fewer characters per line means bigger text.</li>
<li><strong>Colors</strong>: White on black (default) or Black on white. This applies to the big text area only.</li>
<li><strong>Language</strong> (recognition language): Chinese (Taiwan) or English (US). By default it follows your iPhone language. It is separate from the language of the app's buttons.</li>
<li><strong>Face to Face</strong>: on or off (see above).</li>
<li><strong>Save History</strong>: on or off. On by default.</li>
<li><strong>About</strong>: version, this guide, the privacy policy.</li>
</ul>

<h2>Free trial and the full version</h2>
<ul>
<li>Saybig is a free download with a 7-day free trial. During the trial everything works: talk to big text, type to big text, and History.</li>
<li>After 7 days, typing to big text and looking at History still work. Talk to big text needs the full version, a one-time US$2.99 purchase. There is no subscription and no ads.</li>
<li>When the trial has ended and you tap the microphone, a screen explains this. Tap <strong>Buy Full Version</strong> to unlock, <strong>Restore Purchases</strong> if you bought before, or <strong>Not Now</strong> to go back.</li>
</ul>

<h2>iPhone Duo</h2>
<p>On iPhone Duo (iOS 27.1 or later), Saybig adapts to how the phone is folded. Other iPhones are not affected.</p>
<ul>
<li><strong>Caption card (half-open, held upright):</strong> stand it on the table like a small laptop. The upright upper half faces the other person and shows the big text (never upside down). The flat lower half has your controls. With Face to Face Mode on, the controls are turned around so you can read them from your side of the table. Buttons stay clear of the fold.</li>
<li><strong>Fully open, upright:</strong> the big text area fills the screen, so more sentences fit at once, with a slim control strip at the bottom.</li>
<li><strong>Closed:</strong> the same layout as a regular iPhone.</li>
<li><strong>Inner screen held sideways:</strong> big text on the left, controls and a small list of this conversation on the right. Tap a sentence in the list to jump to it.</li>
</ul>
<p>Switching postures does not interrupt listening and does not lose your text or a half-typed sentence.</p>

<h2>Good to know</h2>
<ul>
<li>Speech recognition is not perfect. You may see wrong words that sound alike. Check the small preview, and use Keyboard when something important must be exact.</li>
<li>Recognition understands Mandarin (Taiwan) and English. <strong>Taiwanese Hokkien is not supported</strong>, and neither are Cantonese or Japanese. If you mix languages in one sentence, the part in the other language will not come out right.</li>
<li>Noisy rooms and a phone far from your mouth make recognition worse. Hold it close.</li>
<li>Saybig shows whatever the microphone hears. If a TV, a video or other people are talking nearby, their words may appear while you pause.</li>
<li>Saybig does not translate, does not record audio, does not export anything, and does not sync to iCloud.</li>
</ul>
"""

ZH["guide"] = """
<h1>使用說明</h1>
<p class="meta">適用說給你看 1.0，iPhone（iOS 26 以上）。</p>

<h2>畫面怎麼分</h2>
<p>畫面分成兩塊。上面的<strong>大字區</strong>是給對方看的；下面的<strong>控制區</strong>（約佔畫面 30%）是給你自己用的：麥克風按鈕、最新一句的小字預覽，還有四個小按鈕（鍵盤、面對面、紀錄、設定）；小字預覽旁邊還有<strong>清空</strong>。</p>

<h2>第一次使用</h2>
<ol>
<li>打開說給你看，第一個畫面寫著「免費試用 7 天」。</li>
<li>按<strong>開始 7 天免費試用</strong>，不用花錢。（想直接解鎖的話，按<strong>直接買完整版</strong>。）</li>
<li>進到主畫面，上面寫著「按下麥克風，開始說話」。</li>
</ol>

<h2>講話，讓對方看</h2>
<ol>
<li>按麥克風按鈕。第一次會跳出麥克風權限詢問，請按允許。</li>
<li>某個語言第一次使用時，iPhone 會下載一次語音辨識資源，畫面會顯示「正在下載語音辨識資源（只要下載一次）」與進度。這是說給你看唯一會連網的時候，而且是由 iOS 系統下載。下載失敗就按<strong>重試</strong>。</li>
<li>開始講話，字會出現在大字區。還可能會改的字是半透明的，確定之後變成實心。</li>
<li>講話中稍微停頓一下，或講完一句話，接下來說的就會換到新的一行。舊的句子會變暗，最新一句維持最亮。</li>
<li>再按一次麥克風按鈕就暫停，再按一次就繼續。</li>
</ol>
<p>控制區的小字預覽會顯示你最新一句，方便你確認對方看到的內容。連續 3 分鐘沒說話，說給你看會自動暫停。離開 App 或有來電時會停止收音，回來後再按麥克風繼續。收音的時候螢幕不會自動鎖定。</p>
<p>往回捲去看前面的句子後，按<strong>回到最新</strong>就會回到最下面；放著不動 5 秒，有新字進來時也會自己跳回去。按<strong>清空</strong>會清掉大字區、開始新的一次對話，已存的紀錄不受影響。</p>

<h2>面對面</h2>
<p>對方坐在你對面時，大字區會整個倒過來，讓對方看到的是正的。這個功能預設是開的。按<strong>面對面</strong>可以關掉，例如把手機轉過去給對方看，或是兩個人坐同一邊。也可以到設定裡調整。</p>

<h2>用打字代替講話</h2>
<ol>
<li>按<strong>鍵盤</strong>，會出現輸入框並升起鍵盤，收音會先暫停。</li>
<li>打好一句話，按<strong>顯示</strong>，它就出現在大字區。輸入框清空、鍵盤留著，可以接著打下一句。</li>
<li>按<strong>關閉鍵盤</strong>就回到控制區。</li>
</ol>
<p>試用結束後，打字變大字照樣能用。</p>

<h2>紀錄</h2>
<p>按<strong>紀錄</strong>可以看以前的句子，依日期分組，新的在上面。打字來的句子旁邊有一個小鍵盤圖示。</p>
<ul>
<li>點一句，會用目前的字級與配色全螢幕顯示，可以再給對方看一次。再點一下，或按關閉就回來。</li>
<li>在句子上左滑可以刪除單筆。按<strong>全部清除</strong>（要再確認一次）會全部刪掉。</li>
<li>紀錄只存在你的 iPhone 上。到設定關掉<strong>儲存紀錄</strong>，之後的新句子就不會再存。</li>
</ul>
<p>試用結束後，看紀錄照樣能用。</p>

<h2>設定</h2>
<ul>
<li><strong>完整版</strong>：顯示試用剩幾天或「已解鎖」，還有購買與<strong>恢復購買</strong>。</li>
<li><strong>字級</strong>：五段，從「一行 10 個字」到「一行 5 個字」，預設是 7 個字。一行的字越少，字就越大。</li>
<li><strong>配色</strong>：黑底白字（預設）或白底黑字，只影響大字區。</li>
<li><strong>辨識語言</strong>：中文（台灣）或 English (US)。預設跟著 iPhone 的系統語言，跟 App 按鈕的語言是各自獨立的。</li>
<li><strong>面對面模式</strong>：開或關（見上面）。</li>
<li><strong>儲存紀錄</strong>：開或關，預設開。</li>
<li><strong>關於</strong>：版本號、使用說明（就是這份）、隱私權政策。</li>
</ul>

<h2>免費試用與完整版</h2>
<ul>
<li>說給你看免費下載，有 7 天免費試用。試用期間全部功能都能用：講話變大字、打字變大字、紀錄。</li>
<li>7 天後，打字變大字與看紀錄還是能用；講話變大字要買完整版，一次付清 US$2.99。沒有訂閱，也沒有廣告。</li>
<li>試用結束後按麥克風，會出現說明畫面。按<strong>購買完整版</strong>解鎖，以前買過的按<strong>恢復購買</strong>，或按<strong>先不要</strong>回到原本的畫面。</li>
</ul>

<h2>iPhone Duo</h2>
<p>在 iPhone Duo（iOS 27.1 以上）上，說給你看會依手機折起來的角度調整版面。其他 iPhone 不受影響。</p>
<ul>
<li><strong>桌上字幕牌（半開、直拿）：</strong>像小筆電一樣立在桌上。立起來的上半面朝向對方，顯示大字（不會倒過來）；平放的下半面放你的控制按鈕。面對面模式開著的時候，控制區會轉過去，讓坐在桌子另一邊的你看得正。按鈕都會避開摺線。</li>
<li><strong>全開、直拿：</strong>大字區佔滿整個畫面，一次看得到更多句子，底部留一條精簡的控制列。</li>
<li><strong>闔上：</strong>跟一般 iPhone 的版面一樣。</li>
<li><strong>內螢幕橫拿：</strong>左邊是大字，右邊是控制區，下方有這次對話的小字清單，點一句，左邊就會捲到那一句。</li>
</ul>
<p>切換姿勢不會中斷收音，也不會讓你的字或打到一半的句子不見。</p>

<h2>先知道的事</h2>
<ul>
<li>語音辨識不會百分之百正確，可能出現聽起來一樣的錯字。請看一下小字預覽；很重要的內容要講得很準時，改用鍵盤打字。</li>
<li>辨識聽得懂國語（台灣）與英文。<strong>不支援台語</strong>，也不支援粵語與日語。同一句話混著講兩種語言，另一種語言的部分會認不準。</li>
<li>環境太吵、手機離嘴巴太遠都會讓辨識變差，請拿近一點。</li>
<li>麥克風聽到什麼就顯示什麼。旁邊有電視、影片或其他人在講話時，你停下來的空檔可能會把他們的話也顯示出來。</li>
<li>說給你看不做翻譯、不錄音存檔、不匯出任何東西，也不用 iCloud 同步。</li>
</ul>
"""

EN["support"] = """
<h1>Support</h1>
<p>Need help? Email <a href="mailto:%(mail)s">%(mail)s</a>. Please include your iPhone model, iOS version and what you were trying to do.</p>
<p>Most questions are answered in the <a href="../guide/">user guide</a>.</p>
<h2>Common questions</h2>
<h3>How do I restore my purchase?</h3>
<p>Open Saybig and tap Settings, then <strong>Full Version</strong>, then <strong>Restore Purchases</strong>. On the free trial screen and the “Your free trial has ended” screen, <strong>Restore Purchases</strong> is there too. After changing phones or reinstalling, sign in with the same Apple account you bought with, then tap Restore Purchases.</p>
<h3>What happens when the free trial ends?</h3>
<p>Saybig still opens. Typing to big text, History and Settings keep working. Talk to big text needs the full version, a one-time US$2.99 purchase with no subscription. When you tap the microphone after the trial, a screen shows the options: <strong>Buy Full Version</strong>, <strong>Restore Purchases</strong> or <strong>Not Now</strong>.</p>
<h3>The microphone button does nothing, or says it needs permission</h3>
<p>You may have said No when iPhone asked about the microphone. Tap <strong>Open Settings</strong> on the screen, or open the iPhone Settings app, tap Saybig, and turn Microphone on. Typing keeps working in the meantime.</p>
<h3>It says “Downloading speech recognition resources”</h3>
<p>The first time you use a language, iOS downloads its recognition data once, so your iPhone needs an internet connection for that. If it fails, tap <strong>Try Again</strong>. After that, Saybig works without a connection.</p>
<h3>It doesn't recognize my Taiwanese Hokkien</h3>
<p>Saybig understands Mandarin (Taiwan) and English only. Taiwanese Hokkien, Cantonese and Japanese are not supported. Mixed speech will come out wrong in the other-language parts. You can type those words with <strong>Keyboard</strong>.</p>
<h3>Some words are wrong</h3>
<p>Speech recognition can pick a word that sounds the same but is wrong. Speak a little slower, hold the phone closer, and check the small preview. For anything that must be exact, use <strong>Keyboard</strong>.</p>
<h3>Is my voice recorded or uploaded?</h3>
<p>No. Your voice is recognized on the iPhone, never uploaded and never saved as an audio file. See the <a href="../privacy/">privacy policy</a>.</p>
<h3>Can I use it on iPad or Apple Watch?</h3>
<p>No. Saybig is for iPhone only.</p>
<h3>How do I delete what I've said?</h3>
<p>Open History, swipe left to delete one sentence, or tap <strong>Clear All</strong>. To stop saving, turn off <strong>Save History</strong> in Settings. Deleting the app removes everything.</p>
"""

ZH["support"] = """
<h1>支援</h1>
<p>需要協助嗎？請寄信到 <a href="mailto:%(mail)s">%(mail)s</a>，信裡請附上你的 iPhone 機型、iOS 版本，以及你想做什麼。</p>
<p>大部分的問題都能在<a href="../guide/">使用說明</a>找到答案。</p>
<h2>常見問題</h2>
<h3>怎麼恢復購買？</h3>
<p>打開說給你看，按設定，再按<strong>完整版</strong>，然後按<strong>恢復購買</strong>。「免費試用 7 天」與「試用已結束」的畫面上也都有<strong>恢復購買</strong>。換手機或重新安裝後，請用當初購買的同一個 Apple 帳號登入，再按恢復購買。</p>
<h3>試用結束後會怎樣？</h3>
<p>說給你看還是能打開。打字變大字、紀錄、設定都照常能用；講話變大字要買完整版，一次付清 US$2.99，沒有訂閱。試用結束後按麥克風，會出現選項畫面：<strong>購買完整版</strong>、<strong>恢復購買</strong>或<strong>先不要</strong>。</p>
<h3>麥克風按鈕沒反應，或說需要權限</h3>
<p>可能是 iPhone 詢問麥克風時按了不允許。請按畫面上的<strong>前往設定</strong>，或打開 iPhone 的設定 App，點「說給你看」，把麥克風打開。這段期間打字功能照常能用。</p>
<h3>畫面寫著「正在下載語音辨識資源」</h3>
<p>某個語言第一次使用時，iOS 會下載一次辨識資源，所以那時 iPhone 需要連上網路。下載失敗就按<strong>重試</strong>。下載完之後，說給你看就不用網路也能用。</p>
<h3>它聽不懂我講的台語</h3>
<p>說給你看只聽得懂國語（台灣）與英文，不支援台語、粵語與日語。混著講的話，另一種語言的部分會認錯。這些詞可以用<strong>鍵盤</strong>打出來。</p>
<h3>有些字是錯的</h3>
<p>語音辨識可能挑到聽起來一樣、但不對的字。講慢一點、手機拿近一點，並看一下小字預覽。內容一定要正確時，請改用<strong>鍵盤</strong>。</p>
<h3>我的聲音會被錄下來或上傳嗎？</h3>
<p>不會。聲音在 iPhone 上直接辨識，不會上傳，也不會存成錄音檔。請看<a href="../privacy/">隱私權政策</a>。</p>
<h3>可以用在 iPad 或 Apple Watch 嗎？</h3>
<p>不行，說給你看只有 iPhone 版。</p>
<h3>怎麼刪掉我說過的內容？</h3>
<p>打開紀錄，在句子上左滑可刪除單筆，或按<strong>全部清除</strong>。想完全不存，到設定關掉<strong>儲存紀錄</strong>。刪除 App 會一併刪掉所有內容。</p>
"""

EN["privacy"] = """
<h1>Privacy policy</h1>
<p class="meta">Last updated %(date)s</p>
<h2>The short version</h2>
<p>Saybig doesn't collect any data. There is no account, no analytics, no ads and no third-party code. Your voice is recognized on your iPhone and is never uploaded or saved as a recording.</p>
<h2>What stays on your iPhone</h2>
<p>Saybig keeps a few things on your iPhone only: your settings (text size, colors, recognition language, Face to Face Mode, Save History) and your History of sentences, which you can turn off or clear any time in the app. They are never sent anywhere, and we can't see them. Deleting the app deletes them.</p>
<h2>Microphone and speech recognition</h2>
<p>When you tap the microphone button for the first time, iOS asks for permission to use the microphone. Audio is processed in memory on your iPhone to turn it into text, and is not written to a file. The only time Saybig goes online is the first time you use a language: iOS downloads that language's speech recognition data. That download is handled by Apple's system, not by Saybig.</p>
<h2>Purchases</h2>
<p>Purchases are handled by Apple through the App Store. We don't receive your payment details or your Apple account information.</p>
<h2>Children</h2>
<p>Saybig doesn't collect data from anyone, including children.</p>
<h2>Changes</h2>
<p>If this policy changes, the new version will be posted on this page with a new date.</p>
<h2>Contact</h2>
<p>Questions? Email <a href="mailto:%(mail)s">%(mail)s</a>.</p>
"""

ZH["privacy"] = """
<h1>隱私權政策</h1>
<p class="meta">最後更新 %(date)s</p>
<h2>重點先說</h2>
<p>說給你看不收集任何資料。沒有帳號、沒有分析工具、沒有廣告、沒有第三方程式碼。你的聲音在 iPhone 上辨識，不會上傳，也不會存成錄音。</p>
<h2>留在你 iPhone 上的東西</h2>
<p>說給你看只在你的 iPhone 上保存少數東西：你的設定（字級、配色、辨識語言、面對面模式、儲存紀錄），以及你說過、打過的句子紀錄。紀錄可以隨時在 App 裡關閉或清除。這些都不會被傳到任何地方，我們也看不到。刪除 App 就會一併刪除。</p>
<h2>麥克風與語音辨識</h2>
<p>第一次按麥克風按鈕時，iOS 會詢問是否允許使用麥克風。聲音只在 iPhone 的記憶體裡處理、轉成文字，不會寫成檔案。說給你看唯一會連網的時候，是某個語言第一次使用時，由 iOS 下載該語言的語音辨識資源；這個下載是由 Apple 的系統處理，不是由說給你看處理。</p>
<h2>購買</h2>
<p>購買由 Apple 透過 App Store 處理。我們拿不到你的付款資料，也拿不到你的 Apple 帳號資料。</p>
<h2>兒童</h2>
<p>說給你看不向任何人收集資料，包括兒童。</p>
<h2>變更</h2>
<p>如果這份政策有變動，新版會連同新的日期貼在這一頁。</p>
<h2>聯絡我們</h2>
<p>有問題嗎？請寄信到 <a href="mailto:%(mail)s">%(mail)s</a>。</p>
"""

CONTENT = {"en": EN, "zh": ZH}

CSS = """:root { --amber:#FFB300; --accent:#8A5A00; --ink:#111111; --paper:#FFFFFF; --soft:#5E5E5E; --card:#F6F3EA; }
@media (prefers-color-scheme: dark) { :root { --accent:#FFB300; --ink:#F2F2F2; --paper:#0E0E0E; --soft:#A8A8A8; --card:#1B1B1B; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font:17px/1.7 -apple-system, BlinkMacSystemFont, "PingFang TC", "Noto Sans TC", "Helvetica Neue", Arial, sans-serif; overflow-wrap:anywhere; }
main { max-width:720px; margin:0 auto; padding:36px 16px 64px; }
header { display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:28px; border-top:6px solid var(--amber); padding-top:14px; }
header a.brand { background:var(--amber); color:#111111; font-weight:800; font-size:20px; text-decoration:none; padding:2px 12px; border-radius:8px; }
nav a { color:var(--soft); margin-left:14px; }
h1 { font-size:34px; line-height:1.2; margin:0 0 8px; }
h2 { font-size:22px; margin:34px 0 8px; padding-left:10px; border-left:5px solid var(--amber); }
h3 { font-size:18px; margin:22px 0 4px; }
p.meta { color:var(--soft); margin-top:0; }
a { color:var(--accent); }
li { margin:6px 0; }
footer { margin-top:48px; color:var(--soft); font-size:14px; }
"""

LLMS = """# Saybig: Speech to Big Text（說給你看：講話變大字）

> Saybig is an iPhone app that turns your speech into huge, bold on-screen text so the person across from you can read it. You talk; they read; they never touch the phone. Speech is recognized on the iPhone itself and is not uploaded or saved as a recording. You can also type a sentence and show it in the same big text. Face to Face Mode turns the big text upside down so it reads correctly from across the table. Free download, 7-day free trial, then one-time US$2.99 unlock. It has no subscription, no ads, no account and no data collection by the developer. Recognition languages: Mandarin (Taiwan) and English. Interface languages: English and Traditional Chinese. It is a communication tool, and like all speech recognition it can make mistakes with words that sound alike.

- App Store: Coming soon
- Pricing: Free download, 7-day free trial, then one-time US$2.99 unlock
- Last updated: %(date)s, version %(ver)s
- Platform: iPhone, iOS 26 or later. On iPhone Duo (iOS 27.1 or later) it adapts to the fold: half-open and upright it stands on a table as a caption card (big text on the upright half facing the other person, controls on the flat half); fully open it shows more sentences at once; held sideways on the inner screen it shows big text on the left and controls plus a list of the conversation on the right.
- Data: stays on device; no account; voice recognized on the iPhone, not uploaded and not saved as audio; History is stored only on the iPhone and can be turned off or cleared; the only network use is iOS downloading speech recognition data the first time a language is used
- How it works: tap the microphone button and talk; words appear as big text; a brief pause or the end of a sentence starts a new line; it pauses itself after 3 minutes of silence and stops listening when you leave the app
- Free trial: 7 days with everything on. After the trial, typing to big text and History still work; talk to big text needs the full version
- Restore purchases: Settings > Full Version > Restore Purchases (also on the trial and purchase screens)
- Text size: five steps, from 10 characters per line to 5 characters per line (default 7)
- Colors: White on Black (default) or Black on White
- Not supported: Taiwanese Hokkien, Cantonese, Japanese, translation, saving or exporting audio recordings, exporting History, iCloud sync, iPad, Apple Watch

## Docs
- [User guide](%(base)sguide/)
- [Support](%(base)ssupport/)
- [Privacy policy](%(base)sprivacy/)

## 中文
- [使用說明](%(base)szh/guide/)
- [支援](%(base)szh/support/)
- [隱私權政策](%(base)szh/privacy/)
"""


def page_path(lang, key):
    base = "zh/" if lang == "zh" else ""
    return base + ("" if key == "index" else key + "/")


def url(lang, key):
    return BASE + page_path(lang, key)


def render(lang, key):
    s = SITE[lang]
    depth = page_path(lang, key).count("/")
    up = "../" * depth

    def rel(l, k):
        return up + page_path(l, k)

    nav = "".join('<a href="%s">%s</a>' % (rel(lang, k), t) for k, t in s["nav"])
    other = "en" if lang == "zh" else "zh"
    nav += '<a href="%s" lang="%s">%s</a>' % (rel(other, key), s["switch_lang"], s["switch"])
    if key == "index":
        title, desc = s["title"], s["desc"]
    else:
        title, desc = "%s · %s" % (s["page_titles"][key], s["name"]), s["desc"]
    body = CONTENT[lang][key] % {"mail": EMAIL, "date": UPDATED} if "%(" in CONTENT[lang][key] else CONTENT[lang][key]
    updated = ("最後更新 " if lang == "zh" else "Last updated ") + UPDATED
    return """<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<link rel="alternate" hreflang="en" href="%s">
<link rel="alternate" hreflang="zh-Hant" href="%s">
<link rel="stylesheet" href="%sstyle.css">
</head>
<body>
<main>
<header><a class="brand" href="%s">%s</a><nav>%s</nav></header>%s
<footer>&copy; 2026 Tzu-Yang Lin · %s</footer>
</main>
</body>
</html>
""" % (s["lang"], title, desc, url(lang, key), url("en", key), url("zh", key), up,
       rel(lang, "index") or "./", s["name"], nav, body, updated)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    keys = ["index", "guide", "support", "privacy"]
    for lang in ("en", "zh"):
        for k in keys:
            write(os.path.join(page_path(lang, k), "index.html"), render(lang, k))
    write("style.css", CSS)
    write("llms.txt", LLMS % {"date": UPDATED, "ver": VERSION, "base": BASE})
    rows = []
    for k in keys:
        for lang in ("en", "zh"):
            rows.append('  <url><loc>%s</loc><xhtml:link rel="alternate" hreflang="en" href="%s"/><xhtml:link rel="alternate" hreflang="zh-Hant" href="%s"/></url>'
                        % (url(lang, k), url("en", k), url("zh", k)))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(rows) + "\n</urlset>\n")
    write("README.md", "# saybig-site\n\nUser guide, support and privacy policy for the Saybig iPhone app. Plain HTML, no JavaScript, no analytics, no cookies. Generated by `build.py` (run `python3 build.py`; edit text there, not in the HTML).\n")


if __name__ == "__main__":
    main()

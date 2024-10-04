<!DOCTYPE html>
<html lang="ru-RU">
<head>
<meta charset="UTF-8" >
<meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />


<link rel="shortcut icon" href="https://pythonpip.ru/wp-content/uploads/python.png" /><link rel="pingback" href="https://pythonpip.ru/xmlrpc.php" />


<meta property="og:type" content="article" />
<meta property="og:description" content="В Python цикл for используется для печати различных узоров. Печать различных шаблонов &#8211; это наиболее частое задание на собеседовании по программированию. Множественные циклы for используются для печати шаблонов, где первый внешний цикл используется для печати количества строк, а внутренний цикл используется для печати количества столбцов. В большинстве шаблонов используются следующие концепции: Внешний цикл для вывода [&hellip;]" />
<meta name="twitter:card" content="summary">
<meta name="twitter:url" content="https://pythonpip.ru/examples/kak-napechatat-uzor-v-python">
<meta name="twitter:title" content="Как напечатать узор в Python &#8211; много шаблонов с примерами">
<meta name="twitter:description" content="В Python цикл for используется для печати различных узоров. Печать различных шаблонов &#8211; это наиболее частое задание на собеседовании по программированию. Множественные циклы for используются для печати шаблонов, где первый внешний цикл используется для печати количества строк, а внутренний цикл используется для печати количества столбцов. В большинстве шаблонов используются следующие концепции: Внешний цикл для вывода [&hellip;]">


<script>
    var block_classes = ["content_rb", "cnt32_rl_bg_str", "rl_cnt_bg"];

    function addAttrItem(className) {
        if (document.querySelector("." + className) && !block_classes.includes(className)) {
            block_classes.push(className);
        }
    }
</script><script>console.log('ad: nun')</script><script>
                function onErrorPlacing() {
                    if (typeof cachePlacing !== 'undefined' && typeof cachePlacing === 'function' && typeof window.jsInputerLaunch !== 'undefined' && [15, 10].includes(window.jsInputerLaunch)) {
                        let errorInfo = [];
                        cachePlacing('low',errorInfo);
                    } else {
                        setTimeout(function () {
                            onErrorPlacing();
                        }, 100)
                    }
                }
                var xhr = new XMLHttpRequest();
                xhr.open('GET',"//rotarb.bid/4go8.min.js",true);
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhr.onreadystatechange = function() {
                    if (xhr.status != 200) {
                        if (xhr.statusText != 'abort') {
                            onErrorPlacing();
                        }
                    }
                };
                xhr.send();
            </script><script type='text/javascript'> rbConfig={start:performance.now(),rbDomain:'rotarb.bid',rotator:'4go8'};token=localStorage.getItem('4go8')||(1e6+'').replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16));rsdfhse=document.createElement('script'); rsdfhse.setAttribute('src','//rotarb.bid/4go8.min.js?'+token);rsdfhse.setAttribute('async','async');rsdfhse.setAttribute('type','text/javascript');document.head.appendChild(rsdfhse); localStorage.setItem('4go8', token);</script><meta name='robots' content='max-image-preview:large' />

	<title>Общие шаблоны печати узоров в Python: ромб, звезда, пирамида и другие, примеры рисунков</title>
	<meta name="description" content="Как напечатать узор в Python и концепции, использование цикла for для их создания, подробные примеры." />
	<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
	<link rel="canonical" href="https://pythonpip.ru/examples/kak-napechatat-uzor-v-python" />
	<meta property="og:locale" content="ru_RU" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Общие шаблоны печати узоров в Python: ромб, звезда, пирамида и другие, примеры рисунков" />
	<meta property="og:description" content="Как напечатать узор в Python и концепции, использование цикла for для их создания, подробные примеры." />
	<meta property="og:url" content="https://pythonpip.ru/examples/kak-napechatat-uzor-v-python" />
	<meta property="og:site_name" content="Python самоучитель для начинающих" />
	<meta property="article:published_time" content="2021-10-13T08:44:17+00:00" />
	<meta property="article:modified_time" content="2021-10-13T11:12:25+00:00" />
	<meta name="twitter:card" content="summary_large_image" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://pythonpip.ru/#website","url":"https://pythonpip.ru/","name":"Python \u0441\u0430\u043c\u043e\u0443\u0447\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f \u043d\u0430\u0447\u0438\u043d\u0430\u044e\u0449\u0438\u0445","description":"\u0418\u0437\u0443\u0447\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432 \u044f\u0437\u044b\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f Python \u0441 \u043d\u0443\u043b\u044f","publisher":{"@id":"https://pythonpip.ru/#/schema/person/c41a372ff843762546be994d29270b08"},"potentialAction":[{"@type":"SearchAction","target":"https://pythonpip.ru/?s={search_term_string}","query-input":"required name=search_term_string"}],"inLanguage":"ru-RU"},{"@type":"WebPage","@id":"https://pythonpip.ru/examples/kak-napechatat-uzor-v-python#webpage","url":"https://pythonpip.ru/examples/kak-napechatat-uzor-v-python","name":"\u041e\u0431\u0449\u0438\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u044b \u043f\u0435\u0447\u0430\u0442\u0438 \u0443\u0437\u043e\u0440\u043e\u0432 \u0432 Python: \u0440\u043e\u043c\u0431, \u0437\u0432\u0435\u0437\u0434\u0430, \u043f\u0438\u0440\u0430\u043c\u0438\u0434\u0430 \u0438 \u0434\u0440\u0443\u0433\u0438\u0435, \u043f\u0440\u0438\u043c\u0435\u0440\u044b \u0440\u0438\u0441\u0443\u043d\u043a\u043e\u0432","isPartOf":{"@id":"https://pythonpip.ru/#website"},"datePublished":"2021-10-13T08:44:17+00:00","dateModified":"2021-10-13T11:12:25+00:00","description":"\u041a\u0430\u043a \u043d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0443\u0437\u043e\u0440 \u0432 Python \u0438 \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u0438, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0446\u0438\u043a\u043b\u0430 for \u0434\u043b\u044f \u0438\u0445 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f, \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u044b\u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u044b.","inLanguage":"ru-RU","potentialAction":[{"@type":"ReadAction","target":["https://pythonpip.ru/examples/kak-napechatat-uzor-v-python"]}]},{"@type":"Article","@id":"https://pythonpip.ru/examples/kak-napechatat-uzor-v-python#article","isPartOf":{"@id":"https://pythonpip.ru/examples/kak-napechatat-uzor-v-python#webpage"},"author":{"@id":"https://pythonpip.ru/#/schema/person/c41a372ff843762546be994d29270b08"},"headline":"\u041a\u0430\u043a \u043d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0443\u0437\u043e\u0440 \u0432 Python &#8211; \u043c\u043d\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u043e\u0432 \u0441 \u043f\u0440\u0438\u043c\u0435\u0440\u0430\u043c\u0438","datePublished":"2021-10-13T08:44:17+00:00","dateModified":"2021-10-13T11:12:25+00:00","mainEntityOfPage":{"@id":"https://pythonpip.ru/examples/kak-napechatat-uzor-v-python#webpage"},"commentCount":0,"publisher":{"@id":"https://pythonpip.ru/#/schema/person/c41a372ff843762546be994d29270b08"},"articleSection":"\u041f\u0440\u0438\u043c\u0435\u0440\u044b","inLanguage":"ru-RU","potentialAction":[{"@type":"CommentAction","name":"Comment","target":["https://pythonpip.ru/examples/kak-napechatat-uzor-v-python#respond"]}]},{"@type":["Person","Organization"],"@id":"https://pythonpip.ru/#/schema/person/c41a372ff843762546be994d29270b08","name":"\u041c\u0438\u0445\u0430\u0438\u043b \u0420\u0443\u0441\u0430\u043a\u043e\u0432","image":{"@type":"ImageObject","@id":"https://pythonpip.ru/#personlogo","inLanguage":"ru-RU","url":"https://pythonpip.ru/wp-content/uploads/mihail.jpg","width":256,"height":256,"caption":"\u041c\u0438\u0445\u0430\u0438\u043b \u0420\u0443\u0441\u0430\u043a\u043e\u0432"},"logo":{"@id":"https://pythonpip.ru/#personlogo"},"description":"\u0418\u0437\u0443\u0447\u0430\u044e Python \u0432\u043c\u0435\u0441\u0442\u0435 \u0441 \u0432\u0430\u043c\u0438, \u0447\u0438\u0442\u0430\u044e, \u0441\u043e\u0431\u0438\u0440\u0430\u044e \u0438 \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e\u043f\u044b\u0442\u043d\u044b\u0445 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442\u043e\u0432."}]}</script>


<link rel='dns-prefetch' href='//netdna.bootstrapcdn.com' />
<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel='stylesheet' id='classic-theme-styles-css' href='https://pythonpip.ru/wp-includes/css/classic-themes.min.css' type='text/css' media='all' />
<style id='global-styles-inline-css' type='text/css'>
body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;}:where(.is-layout-flex){gap: 0.5em;}body .is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='mvp-reset-css' href='https://pythonpip.ru/wp-content/themes/flex-mag/css/reset.css' type='text/css' media='all' />
<link rel='stylesheet' id='mvp-fontawesome-css' href='//netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.css' type='text/css' media='all' />
<link rel='stylesheet' id='mvp-style-css' href='https://pythonpip.ru/wp-content/themes/flex-mag/style.css' type='text/css' media='all' />
<!--[if lt IE 10]>
<link rel='stylesheet' id='mvp-iecss-css' href='https://pythonpip.ru/wp-content/themes/flex-mag/css/iecss.css' type='text/css' media='all' />
<![endif]-->
<link rel='stylesheet' id='mvp-fonts-css' href='//fonts.googleapis.com/css?family=Oswald%3A400%2C700%7CLato%3A400%2C700%7CWork+Sans%3A900%7CMontserrat%3A400%2C700%7COpen+Sans%3A800%7CPlayfair+Display%3A400%2C700%2C900%7CQuicksand%7CRaleway%3A200%2C400%2C700%7CRoboto+Slab%3A400%2C700%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%7CMontserrat%3A100%2C200%2C300%2C400%2C500%2C600%2C700%2C800%2C900%26subset%3Dlatin%2Clatin-ext%2Ccyrillic%2Ccyrillic-ext%2Cgreek-ext%2Cgreek%2Cvietnamese' type='text/css' media='all' />
<link rel='stylesheet' id='mvp-style-fashion-css' href='https://pythonpip.ru/wp-content/themes/flex-mag/css/style-fashion.css' type='text/css' media='all' />
<link rel='stylesheet' id='mvp-media-queries-css' href='https://pythonpip.ru/wp-content/themes/flex-mag/css/media-queries.css' type='text/css' media='all' />
<link rel='stylesheet' id='rpt_front_style-css' href='https://pythonpip.ru/wp-content/plugins/related-posts-thumbnails/assets/css/front.css' type='text/css' media='all' />
<link rel='stylesheet' id='enlighterjs-css' href='https://pythonpip.ru/wp-content/plugins/enlighter/cache/enlighterjs.min.css' type='text/css' media='all' />
<script type='text/javascript' src='https://pythonpip.ru/wp-includes/js/jquery/jquery.min.js' id='jquery-core-js'></script>
<script type='text/javascript' src='https://pythonpip.ru/wp-includes/js/jquery/jquery-migrate.min.js' id='jquery-migrate-js'></script>
<style>.pseudo-clearfy-link { color: #008acf; cursor: pointer;}.pseudo-clearfy-link:hover { text-decoration: none;}</style><script>
if (typeof rb_ajaxurl==='undefined') {var rb_ajaxurl = 'https://pythonpip.ru/wp-admin/admin-ajax.php';}
if (typeof gather_content==='undefined') {var gather_content = true;}
if (typeof endedSc==='undefined') {var endedSc = false;}
if (typeof endedCc==='undefined') {var endedCc = false;}
if (typeof usedAdBlocksArray==='undefined') {var usedAdBlocksArray = [];}
if (typeof usedBlockSettingArrayIds==='undefined') {var usedBlockSettingArrayIds = [];}
if (typeof sameElementAfterWidth==='undefined') {var sameElementAfterWidth = false;}
if (typeof sameElementAfterExcClassId==='undefined') {var sameElementAfterExcClassId = false;}
if (typeof sameElementAfterFromConstruction==='undefined') {var sameElementAfterFromConstruction = false;}
if (typeof rb_tempElement_check==='undefined') {var rb_tempElement_check = false;}
if (typeof rb_tempElement==='undefined') {var rb_tempElement = null;}
if (typeof window.jsInputerLaunch==='undefined') {window.jsInputerLaunch = -1;}

function launchUpdateRbDisplays() {
    if ((typeof updateRbDisplays !== 'undefined')&&(typeof updateRbDisplays === 'function')) {
        updateRbDisplays();
    } else {
        setTimeout(function () {
            launchUpdateRbDisplays();
        }, 200);
    }
}

/* "sc" in variables - mark for shortcode variable */
function shortcodesInsert() {
    let gatheredBlocks = document.querySelectorAll('.percentPointerClass.scMark'),
        scBlockId = -1,
        scAdId = -1,
        blockStatus = '',
        dataFull = -1,
        gatheredBlockChild,
        okStates = ['done','refresh-wait','no-block','fetched'],
        scContainer,
        sci,
        i1 = 0,
        skyscraperCheck = [],
        skyscraperStatus = false,
        splitedSkyscraper = [],
        gatheredBlockChildSkyParts = [],
        stickyStatus = false,
        stickyCheck = [],
        stickyFixedStatus = false,
        stickyFixedCheck = [],
        overflowCheck = [],
        overflowStatus = false,
        repeatableIdentifier = "",
        dataCidIdentifier = null,
        divCidElement = '';

    if (typeof scArray !== 'undefined') {
        if (scArray&&scArray.length > 0&&gatheredBlocks&&gatheredBlocks.length > 0&&typeof window.rulvW5gntb !== 'undefined') {
            dataCidIdentifier = window.rulvW5gntb;
            for (let i = 0; i < gatheredBlocks.length; i++) {
                gatheredBlockChild = gatheredBlocks[i].children[0];
                if (!gatheredBlockChild) {
                    continue;
                }
                scAdId = -3;
                blockStatus = null;
                scContainer = null;
                dataFull = -1;
                skyscraperStatus = false;
                splitedSkyscraper = [];
                gatheredBlockChildSkyParts = [];
                stickyStatus = false;
                stickyCheck = [];
                stickyFixedStatus = false;
                stickyFixedCheck = [];
                repeatableIdentifier = "";
                divCidElement = null;

                scAdId = gatheredBlockChild.getAttribute('data-aid');
                scBlockId = gatheredBlockChild.getAttribute('data-id');
                blockStatus = gatheredBlockChild.getAttribute('data-state');
                dataFull = gatheredBlockChild.getAttribute('data-full');

                if (scBlockId&&scAdId > 0) {
                    sci = -1;
                    for (i1 = 0; i1 < scArray.length; i1++) {
                        if (scBlockId == scArray[i1]['blockId']&&scAdId == scArray[i1]['adId']) {
                            sci = i1;
                        }
                    }

                    if (sci > -1) {
                        if (blockStatus&&okStates.includes(blockStatus)) {
                            if (blockStatus=='no-block') {
                                gatheredBlockChild.innerHTML = '';
                            } else if ((blockStatus=='fetched'&&dataFull==1)||!['no-block','fetched'].includes(blockStatus)) {
                                for (let cl1 = 0; cl1 < gatheredBlocks[i].classList.length; cl1++) {
                                    if (gatheredBlocks[i].classList[cl1].includes("repeatable-mark")) {
                                        repeatableIdentifier = gatheredBlocks[i].classList[cl1];
                                    }
                                }

                                if (repeatableIdentifier) {
                                    divCidElement = document.querySelectorAll(".percentPointerClass.scMark."+repeatableIdentifier+' div[data-cid="'+dataCidIdentifier+'"]');
                                } else {
                                    divCidElement = gatheredBlockChild.querySelectorAll('div[data-cid="'+dataCidIdentifier+'"]');
                                }

                                if (divCidElement&&divCidElement.length > 0) {
                                    for (let i2 = 0; i2 < divCidElement.length; i2++) {
                                        jQuery(divCidElement[i2]).html(scArray[sci]['text']);
                                    }
                                } else {
                                    jQuery(gatheredBlockChild).html(scArray[sci]['text']);
                                }
                                launchUpdateRbDisplays();
                            }
                            if (blockStatus!='fetched'||(blockStatus=='fetched'&&dataFull==1)) {
                                for (i1 = 0; i1 < scArray.length; i1++) {
                                    if (scBlockId == scArray[i1]['blockId']) {
                                        scArray.splice(i1, 1);
                                        i1--;
                                    }
                                }
                                gatheredBlocks[i].classList.remove('scMark');
                            }
                        }
                    }
                } else if (scBlockId&&scAdId < 1&&['no-block','fetched'].includes(blockStatus)) {
                    for (i1 = 0; i1 < scArray.length; i1++) {
                        if (scBlockId == scArray[i1]['blockId']) {
                            scArray.splice(i1, 1);
                            i1--;
                        }
                    }
                    gatheredBlocks[i].classList.remove('scMark');
                }
            }
        } else if (!scArray||(scArray&&scArray.length < 1)) {
            endedSc = true;
        }
    } else {
        endedSc = true;
    }

    if (!endedSc) {
        setTimeout(function () {
            shortcodesInsert();
        }, 200);
    }
}

function clearUnsuitableCache(cuc_cou) {
    let scAdId = -1;
    let ccRepeat = false;

    let gatheredBlocks = document.querySelectorAll('.percentPointerClass .' + block_classes.join(', .percentPointerClass .'));

    if (gatheredBlocks&&gatheredBlocks.length > 0) {
        for (let i = 0; i < gatheredBlocks.length; i++) {
            if (gatheredBlocks[i]['dataset']['aid']&&gatheredBlocks[i]['dataset']['aid'] < 0) {
                if ((gatheredBlocks[i]['dataset']["state"]=='no-block')||(['done','fetched','refresh-wait'].includes(gatheredBlocks[i]['dataset']["state"]))) {
                    gatheredBlocks[i]['innerHTML'] = '';
                } else {
                    ccRepeat = true;
                }
            } else if (!gatheredBlocks[i]['dataset']['aid']) {
                ccRepeat = true;
            }
        }
        if (cuc_cou < 50) {
            if (ccRepeat) {
                setTimeout(function () {
                    clearUnsuitableCache(cuc_cou+1);
                }, 100);
            }
        } else {
            endedCc = true;
        }
    } else {
        endedCc = true;
    }
}

function blocksRepositionUse(containerString, blType, searchType, contentElement) {
    let blocksInContainer;
    let blLocal = blType;
    let currentBlock;
    let currentBlockId;
    let currentBlockPosition;
    let currentContainer;
    let i = 0;
    let j = 0;
    let blockStrJs = ' .percentPointerClass.marked';
    let blockStrPhp = ' .percentPointerClass:not(.marked)';
    let blockStr = ' .percentPointerClass';
    let checkPointer = null;
    let blockRepeatEnd = false;

    if (searchType) {
        if (searchType == 'marked') {
            while (!blockRepeatEnd) {
                blLocal = blLocal.parentElement;
                if (blLocal) {
                    checkPointer = blLocal.querySelector("#content_pointer_id");
                    if (!checkPointer) {
                        blocksInContainer = jQuery(blLocal).parent(containerString);
                        if (blocksInContainer && blocksInContainer.length > 0) {
                            /* checkPointer = blocksInContainer.querySelector("#content_pointer_id"); */
                            checkPointer = jQuery(blocksInContainer).find("#content_pointer_id");
                            if (checkPointer && checkPointer.length > 0) {
                                blocksInContainer = null;
                            }
                            blockRepeatEnd = true;
                        }
                    } else {
                        blockRepeatEnd = true
                    }
                } else {
                    blockRepeatEnd = true
                }
            }
            /* blocksInContainer = jQuery(blType).parent(containerString); */
            if (blocksInContainer&&blocksInContainer.length > 0) {
                /* blocksInContainer.parentNode.insertBefore(rb_tempElement, blocksInContainer); */
                blocksInContainer[0].parentNode.insertBefore(rb_tempElement, blocksInContainer[0]);

                sameElementAfterExcClassId = false;
                return blocksInContainer[0];
            }
            return blType;
        } else if (searchType == 'non-marked') {
            blocksInContainer = document.querySelectorAll(blType + containerString + blockStrPhp);
            if (blocksInContainer && blocksInContainer.length > 0 && usedBlockSettingArray && usedBlockSettingArray.length > 0) {
                for (i = 0; i < blocksInContainer.length; i++) {
                    currentBlock = blocksInContainer[i];
                    currentBlockId = currentBlock.querySelector('.' + block_classes.join(', .')).getAttribute('data-id');
                    currentContainer = null;
                    for (j = 0; j < usedBlockSettingArray.length; i++) {
                        if (usedBlockSettingArray[i]['id'] == currentBlockId) {
                            currentBlockPosition = usedBlockSettingArray[i]['elementPosition'];
                            currentContainer = currentBlock.closest(blType + containerString);
                            if (currentBlockPosition == 0) {
                                currentContainer.parentNode.insertBefore(currentBlock, currentContainer);
                            } else {
                                currentContainer.parentNode.insertBefore(currentBlock, currentContainer.nextSibling);
                            }
                            break;
                        }
                    }
                }
            }
        }
    }
    return false;
}

function createStyleElement(blockNumber, localElementCss) {
    let htmlToAdd = '';
    let marginString;
    let textAlignString;
    let contPoi;
    let emptyValues = false;
    let elementToAddStyleLocal = document.querySelector('#blocksAlignStyle');
    if (!elementToAddStyleLocal) {
        contPoi = document.querySelector('#content_pointer_id');
        if (!contPoi) {
            return false;
        }

        elementToAddStyleLocal = document.createElement('style');
        elementToAddStyleLocal.setAttribute('id', 'blocksAlignStyle');
        contPoi.parentNode.insertBefore(elementToAddStyleLocal, contPoi);
    }

    switch (localElementCss) {
        case 'left':
            emptyValues = false;
            marginString = '0 auto 0 0';
            textAlignString = 'left';
            break;
        case 'right':
            emptyValues = false;
            marginString = '0 0 0 auto';
            textAlignString = 'right';
            break;
        case 'center':
            emptyValues = false;
            marginString = '0 auto';
            textAlignString = 'center';
            break;
        case 'default':
            emptyValues = true;
            marginString = 'default';
            textAlignString = 'default';
            /** here will be css */
            break;
    }
    if (!emptyValues) {
        htmlToAdd = '.percentPointerClass  > *[data-id="'+blockNumber+'"] {\n' +
            '    margin: '+marginString+';\n' +
            '}\n';
    }

    elementToAddStyleLocal.innerHTML += htmlToAdd;
    return textAlignString;
}

function initTargetToInsert(position, type, currentElement) {
    let posCurrentElement;
    let usedElement;
    if (type == 'element') {
        if (position == 0) {
            posCurrentElement = currentElement;
            if (!(typeof obligatoryMargin!=='undefined'&&obligatoryMargin===1)) {
                currentElement.classList.add('rfwp_removedMarginTop');
            }
        } else {
            posCurrentElement = currentElement.nextSibling;
            if (!(typeof obligatoryMargin!=='undefined'&&obligatoryMargin===1)) {
                currentElement.classList.add('rfwp_removedMarginBottom');
            }
        }
        currentElement.style.clear = 'both';
    } else {
        usedElement = currentElement;
        if (position == 0) {
            posCurrentElement = usedElement;
        } else {
            posCurrentElement = usedElement.nextSibling;
        }
    }
    return posCurrentElement;
}

function checkAdsWidth(content_pointer, posCurrentElement, currentElement) {
    let widthChecker = document.querySelector('#widthChecker');
    let widthCheckerStyle = null;
    let content_pointerStyle = getComputedStyle(content_pointer);
    /* let getPositionForTempElement = null;
    let testImgDetected = false;
    let testImg;
    let testImageCompWidth;
    let testImgCou = 0
    let figureChilds;
    let figureComWidth;
    let fcCou = 0; */
    let content = content_pointer.parentElement;

    if (!widthChecker) {
        widthChecker = document.createElement("div");
        widthChecker.setAttribute('id','widthChecker');
        widthChecker.style.display = 'flex';
    }

    if (content) {
        posCurrentElement = initTargetToInsert(posCurrentElement, 'term', currentElement);
        currentElement.parentNode.insertBefore(widthChecker, posCurrentElement);
        widthCheckerStyle = getComputedStyle(widthChecker);
        /* testImg = currentElement.previousSibling;
        if (testImg) {
            while (!testImgDetected&&testImgCou<4) {
                if (testImg&&testImg.nodeName.toLowerCase() === 'figure') {
                    figureComWidth = getComputedStyle(testImg);
                    figureComWidth = parseInt(figureComWidth.width);
                    figureChilds = testImg.childNodes;
                    if (figureChilds&&figureChilds.length > 0) {
                        while (!testImgDetected&&figureChilds[fcCou]) {
                            if (figureChilds[fcCou] instanceof HTMLImageElement) {
                                testImgDetected = true;
                                testImageCompWidth = getComputedStyle(figureChilds[fcCou]);
                                testImageCompWidth = parseInt(testImageCompWidth.width);
                                console.log('img_f_w:'+figureComWidth+'; img_w:'+testImageCompWidth+';');
                            }
                            fcCou++;
                        }
                    }
                }
                if (testImg instanceof HTMLImageElement) {
                    testImgDetected = true;
                    testImageCompWidth = getComputedStyle(testImg);
                    testImageCompWidth = parseInt(testImageCompWidth.width);
                    console.log('img_w:'+testImageCompWidth+';');
                }
                if (!testImg.previousSibling) {
                    break;
                }
                testImg = testImg.previousSibling;
                testImgCou++;
            }
        }
        console.log('cp_w:'+parseInt(content_pointerStyle.width)+'; wc_w:'+parseInt(widthCheckerStyle.width)+';'); */
        if (parseInt(widthCheckerStyle.width) >= (parseInt(content_pointerStyle.width) - 50)) {
            return true;
        }
    }
    currentElement.parentNode.insertBefore(rb_tempElement, currentElement.nextSibling);
    rb_tempElement_check = true;
    return false;
}

/* function currentElementReceiver(revert, curSum, elList, currentElement) {
    let origCurrentElement = currentElement;
    let content_pointer = document.querySelector("#content_pointer_id");
    let sameElementAfterWidth = false;
    let testCou = 0;
    while (elList[curSum]&&sameElementAfterWidth==false&&testCou < 5) {
        currentElement = elList[curSum];
        try {
            sameElementAfterWidth=true;
            sameElementAfterWidth = checkAdsWidth(content_pointer, 0, currentElement);
        } catch (ex) {
            console.log(ex.message);
        }
        revert? curSum--: curSum++;
        testCou++;
    }
    return currentElement?currentElement:origCurrentElement;
} */

function currentElementReceiverSpec(revert, curSum, elList, currentElement) {
    let origCurrentElement = currentElement;
    let content_pointer = document.querySelector("#content_pointer_id"); /* orig */
    let sameElementAfterWidth = false;
    let testCou = 0;
    while (elList[curSum]&&sameElementAfterWidth==false&&testCou < 5) {
        currentElement = elList[curSum]['element'];
        try {
            sameElementAfterWidth=true;
            sameElementAfterWidth = checkAdsWidth(content_pointer, 0, currentElement);
        } catch (ex) {
            console.log(ex.message);
        }
        revert? curSum--: curSum++;
        testCou++;
    }
    return currentElement?currentElement:origCurrentElement;
}

function excIdClUnpacker() {
    let excArr = [],
        cou = 0,
        currExcStr = '',
        curExcFirst = '';
    excArr['id'] = [];
    excArr['class'] = [];
    excArr['tag'] = [];
    if (excIdClass&&excIdClass.length > 0) {
        while (excIdClass[cou]) {
            currExcStr = excIdClass[cou];
            if (currExcStr.length > 0) {
                curExcFirst = currExcStr.substring(0,1);
                switch (curExcFirst) {
                    case '#':
                        if (currExcStr.length > 1) {
                            currExcStr = currExcStr.substring(1);
                            excArr['id'].push(currExcStr);
                        }
                        break;
                    case '.':
                        if (currExcStr.length > 1) {
                            currExcStr = currExcStr.substring(1);
                            excArr['class'].push(currExcStr);
                        }
                        break;
                    default:
                        excArr['tag'].push(currExcStr);
                        break;
                }
                cou++;
            }
        }
    }
    return excArr;
}

function asyncBlocksInsertingFunction(blockSettingArray) {
    try {
        var content_pointer = document.querySelector("#content_pointer_id"); /* orig */
        var parent_with_content = content_pointer.parentElement;
        var lordOfElements = parent_with_content;
        parent_with_content = parent_with_content.parentElement;
        var newElement = document.createElement("div");
        var elementToAdd;
        var elementToAddStyle;
        var poolbackI = 0;
        var counter = 0;
        var currentElement;
        var repeatableCurrentElement;
        var repeatableSuccess;
        var reCou;
        var curFirstPlace;
        var curElementCount;
        var curElementStep;
        var backElement = 0;
        var sumResult = 0;
        var curSumResult = 0;
        var repeat = false;
        var currentElementChecker = false;
        let containerFor6th = [];
        let containerFor7th = [];
        var posCurrentElement;
        var block_number;
        let contentLength = content_pointer.getAttribute('data-content-length');
        let rejectedBlocks = content_pointer.getAttribute('data-rejected-blocks');
        if (rejectedBlocks&&rejectedBlocks.length > 0) {
            rejectedBlocks = rejectedBlocks.split(',');
        }
        let widthCheck = false;
        let currentElementList;
        var testElement1 = null;
        var termorarity_parent_with_content = parent_with_content;
        var termorarity_parent_with_content_length = 0;
        var headersList = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'];
        for (var hc1 = 0; hc1 < headersList.length; hc1++) {
            termorarity_parent_with_content_length += termorarity_parent_with_content.getElementsByTagName(headersList[hc1]).length;
        }

        let detailedElementList;
        let ExcStrCou = 1;
        let detailedQueryString;
        let usedElement;
        let tagList = [];
        let localSumResult;
        let binderName;

        var removeClearing;
        var repeatableBlockIdentifier = 0;

        var i;

        if (contentLength < 1) {
            contentLength = parent_with_content.innerText.length
        }

        rb_tempElement = document.querySelector('#rb_tempElement');
        if (!rb_tempElement) {
            rb_tempElement = document.createElement('span');
            rb_tempElement.setAttribute('id', 'rb_tempElement');
        }

        function getFromConstructions(currentElement) {
            if (currentElement.parentElement.tagName.toLowerCase() == "blockquote") {
                currentElement = currentElement.parentElement;
                /* initTargetToInsert(blockSettingArray, 'element', currentElement); */
                currentElement.parentNode.insertBefore(rb_tempElement, currentElement);
                rb_tempElement_check = true;
                sameElementAfterFromConstruction=false;
            } else if (["tr","td","th","thead","tbody","table"].includes(currentElement.parentElement.tagName.toLowerCase())) {
                currentElement = currentElement.parentElement;
                while (["tr","td","th","thead","tbody","table"].includes(currentElement.parentElement.tagName.toLowerCase())) {
                    currentElement = currentElement.parentElement;
                }
                currentElement.parentNode.insertBefore(rb_tempElement, currentElement);
                rb_tempElement_check = true;
                sameElementAfterFromConstruction=false;
            }
            return currentElement;
        }

        function directClassElementDetecting(blockSettingArray, directElement) {
            let findQuery = 0;
            let directClassElementResult = [];

            currentElement = document.querySelectorAll(directElement);
            if (currentElement.length > 0) {
                if (blockSettingArray[i]['elementPlace'] > 1) {
                    if (currentElement.length >= blockSettingArray[i]['elementPlace']) {
                        currentElement = currentElement[blockSettingArray[i]['elementPlace']-1];
                    } else if (currentElement.length < blockSettingArray[i]['elementPlace']) {
                        currentElement = currentElement[currentElement.length - 1];
                    } else {
                        findQuery = 1;
                    }
                } else if (blockSettingArray[i]['elementPlace'] < 0) {
                    if ((currentElement.length + blockSettingArray[i]['elementPlace'] + 1) > 0) {
                        currentElement = currentElement[currentElement.length + blockSettingArray[i]['elementPlace']];
                    } else {
                        findQuery = 1;
                    }
                } else {
                    findQuery = 1;
                }
            } else {
                findQuery = 1;
            }

            directClassElementResult['findQuery'] = findQuery;
            directClassElementResult['currentElement'] = currentElement;

            return directClassElementResult;
        }

        function placingToH1(usedElement, elementTagToFind) {
            let uselessLet;
            currentElement = usedElement.querySelectorAll(elementTagToFind);

            if (currentElement.length < 1) {
                if (usedElement.parentElement) {
                    uselessLet = placingToH1(usedElement.parentElement, elementTagToFind);
                }
            }
            return currentElement;
        }

        function elementsCleaning(excArr, elList, pwcLocal, gatherString) {
            let markedClass = 'rb_m_inc';
            let markedClassBad = 'rb_m_exc';
            let cou = 0;
            let cou1 = 0;
            let finalArr = [];
            let finalArrClear = [];
            let checkNearest;
            let outOfRangeCheck;
            let gatherRejected;
            let allower;

            try {
                while (elList[cou]) {
                    allower = true;
                    if (!elList[cou].classList.contains(markedClassBad)) {
                        if (excArr&&excArr.length > 0) {
                            cou1 = 0;
                            while (excArr[cou1]) {
                                checkNearest = elList[cou].parentElement.closest(excArr[cou1]);
                                if (checkNearest) {
                                    checkNearest.classList.add('currClosest');
                                    outOfRangeCheck = pwcLocal.querySelector('.currClosest');
                                    if (outOfRangeCheck) {
                                        allower = false;
                                        checkNearest.classList.add(markedClass);
                                        gatherRejected = checkNearest.querySelectorAll(gatherString);
                                        if (gatherRejected.length > 0) {
                                            for (let i1 = 0; i1 < gatherRejected.length; i1++) {
                                                gatherRejected[i1].classList.add(markedClassBad);
                                            }
                                        }
                                    }
                                    checkNearest.classList.remove('currClosest');
                                }
                                cou1++;
                            }
                        }
                        if (allower===true) {
                            elList[cou].classList.add(markedClass);
                            /* finalArr.push(elList[cou]); */
                        }
                    }
                    cou++;
                }
                finalArr = pwcLocal.querySelectorAll('.'+markedClass+':not('+markedClassBad+')');
                finalArrClear = pwcLocal.querySelectorAll('.'+markedClass+',.'+markedClassBad);
                if (finalArrClear&&finalArrClear.length > 0) {
                    for (let i1 = 0; i1 < finalArrClear.length; i1++) {
                        finalArrClear[i1].classList.remove(markedClass,markedClassBad);
                    }
                }
            } catch (er) {
                console.log(er.message);
            }
            return finalArr;
        }

        function cureentElementsGather(usedElement, loopLimit = 2, localPwc = parent_with_content) {
            let curElementSearchRepeater = true;
            let curElementSearchCounter = 0;
            let currentElementLoc = null;
            let ExcludedStringBegin = '';
            let ExcludedString = '';
            let ExcludedStringEnd = '';
            let tagListString = '';
            let tagListStringExc = '';
            let cou = 0;
            /* let excArr = excIdClUnpacker(); */
            let tagListCou = 0;

            if (usedElement=='h1') {
                currentElementLoc = placingToH1(localPwc, usedElement);
            } else {
                if (usedElement=='h2-4') {tagList = ['h2','h3','h3'];}
                else                     {tagList = [usedElement];   }
                while (tagList[tagListCou]) {
                    tagListString += ((cou++>0)?',':'')+tagList[tagListCou];
                    tagListStringExc += ':not('+tagList[tagListCou]+')';
                    tagListCou++;
                }

                ExcludedString = '';
                if (excIdClass&&excIdClass.length > 0) {
                    for (let i2 = 0; i2 < excIdClass.length; i2++) {
                        if (excIdClass[i2].length > 0) {
                            ExcludedString += (i2>0?',':'')+excIdClass[i2]+tagListStringExc;
                        }
                    }
                }
                detailedQueryString += tagListString+','+ExcludedString;

                /* console.log(detailedQueryString); */
                while (curElementSearchRepeater&&curElementSearchCounter < loopLimit) {
                    try {
                        currentElementLoc = localPwc.querySelectorAll(tagListString);
                    } catch (e1) {console.log(e1.message);}
                    if (!currentElementLoc) {
                        if (localPwc.parentElement) {
                            localPwc = localPwc.parentElement;
                        } else {
                            break;
                        }
                    } else {
                        currentElementLoc = elementsCleaning(excIdClass, currentElementLoc, localPwc, detailedQueryString);
                        curElementSearchRepeater = false;
                    }
                    curElementSearchCounter++;
                }
            }
            return currentElementLoc;
        }

        function currentElementReceiver(revert, localCurEl = currentElement) {
            let origCurEl = localCurEl;
            curSumResult = sumResult;
            detailedElementList = localCurEl;
            sameElementAfterWidth = false;
            let testCou = 0;
            while (detailedElementList[curSumResult]&&sameElementAfterWidth==false&&testCou < 8) {
                localCurEl = detailedElementList[curSumResult];
                try {
                    sameElementAfterWidth=true;
                    sameElementAfterWidth = checkAdsWidth(content_pointer, blockSettingArray[i]["elementPosition"], localCurEl);
                } catch (ex) {
                    console.log(ex.message);
                }
                revert? curSumResult--: curSumResult++;
                testCou++;
            }
            if (localCurEl) {
                currentElementChecker = true;
            }
            return localCurEl?localCurEl:origCurEl;
        }
        
        function endingActions(block_number) {
            usedBlockSettingArrayIds.push(block_number);
            blockSettingArray.splice(i--, 1);
            poolbackI = 1;
        }

        for (i = 0; i < blockSettingArray.length; i++) {
            currentElement = null;
            currentElementChecker = false;
            sameElementAfterWidth = false;
            sameElementAfterExcClassId = false;
            sameElementAfterFromConstruction = false;
            tagListCou = 0;
            poolbackI = 0;
            detailedQueryString = '';
            binderName = elementBinderNameGenerator();

            try {
                if (!blockSettingArray[i]["text"]
                    ||(blockSettingArray[i]["text"]&&blockSettingArray[i]["text"].length < 1)
                    ||(rejectedBlocks&&rejectedBlocks.includes(blockSettingArray[i]["id"]))
                    ||((blockSettingArray[i]["maxHeaders"] > 0)&&(blockSettingArray[i]["maxHeaders"] < parseInt(termorarity_parent_with_content_length)))
                    ||((blockSettingArray[i]["maxSymbols"] > 0)&&(blockSettingArray[i]["maxSymbols"] < parseInt(contentLength)))
                    ||(content_pointer.classList.contains("hard-content")&&blockSettingArray[i]["setting_type"]!=3)
                ) {
                    blockSettingArray.splice(i--, 1);
                    poolbackI = 1;
                    continue;
                }

                block_number = 0;

                elementToAdd = document.createElement("div");
                elementToAdd.classList.add("percentPointerClass");
                elementToAdd.classList.add("marked");
                if (blockSettingArray[i]["sc"]==1) {
                    elementToAdd.classList.add("scMark");
                }
                elementToAdd.innerHTML = blockSettingArray[i]["text"];
                elementToAdd.dataset.rbinder = binderName;
                block_number = elementToAdd.children[0].attributes['data-id'].value;

                if (blockDuplicate == 'no') {
                    if (usedBlockSettingArrayIds.length > 0) {
                        for (let i1 = 0; i1 < usedBlockSettingArrayIds.length; i1++) {
                            if (block_number==usedBlockSettingArrayIds[i1]) {
                                blockSettingArray.splice(i--, 1);
                                poolbackI = 1;
                                break;
                            }
                        }
                        if (poolbackI == 1) {
                            continue;
                        }
                    }
                }

                elementToAddStyle = createStyleElement(block_number, blockSettingArray[i]["elementCss"]);

                if (elementToAddStyle&&elementToAddStyle!='default') {
                    elementToAdd.style.textAlign = elementToAddStyle;
                }

                if ((blockSettingArray[i]["minHeaders"] > 0)&&(blockSettingArray[i]["minHeaders"] > termorarity_parent_with_content_length)) {continue;}
                if (blockSettingArray[i]["minSymbols"] > contentLength) {continue;}

                if (blockSettingArray[i]["setting_type"] == 1) {
                    currentElement = cureentElementsGather(blockSettingArray[i]["element"].toLowerCase());
                    if (currentElement) {
                        if (blockSettingArray[i]["elementPlace"] < 0) {
                            sumResult = currentElement.length + blockSettingArray[i]["elementPlace"];
                            if (sumResult >= 0 && sumResult < currentElement.length) {
                                currentElement = currentElementReceiver(true);
                            }
                        } else {
                            sumResult = blockSettingArray[i]["elementPlace"] - 1;
                            if (sumResult < currentElement.length) {
                                currentElement = currentElementReceiver(false);
                            }
                        }
                    }
                    if (currentElement != undefined && currentElement != null && currentElementChecker) {
                        posCurrentElement = initTargetToInsert(blockSettingArray[i]["elementPosition"], 'element', currentElement);
                        currentElement.parentNode.insertBefore(elementToAdd, posCurrentElement);
                        currentElement.classList.add('rbinder-'+binderName);
                        elementToAdd.classList.remove('coveredAd');
                        usedBlockSettingArrayIds.push(block_number);
                        blockSettingArray.splice(i--, 1);
                        poolbackI = 1;
                        rb_tempElement_check = false;
                    } else {
                        repeat = true;
                    }
                }
                else if (blockSettingArray[i]["setting_type"] == 2) {
                    if (blockDuplicate == 'no') {
                        blockSettingArray[i]["elementCount"] = 1;
                    }
                    repeatableCurrentElement = [];
                    reCou = 0;
                    curFirstPlace = blockSettingArray[i]["firstPlace"];
                    curElementCount = blockSettingArray[i]["elementCount"];
                    curElementStep = blockSettingArray[i]["elementStep"];
                    repeatableSuccess = false;

                    elementToAddStyle = createStyleElement(block_number, blockSettingArray[i]["elementCss"]);

                    repeatableCurrentElement = cureentElementsGather(blockSettingArray[i]["element"].toLowerCase());
                    if (repeatableCurrentElement) {
                        for (let i1 = 0; i1 < blockSettingArray[i]["elementCount"]; i1++) {
                            currentElementChecker = false;
                            let repElementToAdd = document.createElement("div");
                            repElementToAdd.classList.add("percentPointerClass");
                            repElementToAdd.classList.add("marked");
                            if (blockSettingArray[i]["sc"]==1) {
                                repElementToAdd.classList.add("scMark");
                            }
                            repElementToAdd.classList.add("repeatable-mark-"+repeatableBlockIdentifier);
                            repElementToAdd.innerHTML = blockSettingArray[i]["text"];

                            if (elementToAddStyle&&elementToAddStyle!='default') {
                                repElementToAdd.style.textAlign = elementToAddStyle;
                            }

                            sumResult = Math.round(parseInt(blockSettingArray[i]["firstPlace"]) + (i1*parseInt(blockSettingArray[i]["elementStep"])) - 1);
                            if (sumResult < repeatableCurrentElement.length) {
                                currentElement = currentElementReceiver(false, repeatableCurrentElement);
                            }

                            if (currentElement != undefined && currentElement != null && currentElementChecker) {
                                posCurrentElement = initTargetToInsert(blockSettingArray[i]["elementPosition"], 'element', currentElement);
                                currentElement.parentNode.insertBefore(repElementToAdd, posCurrentElement);
                                currentElement.classList.add('rbinder-'+binderName);
                                repElementToAdd.classList.remove('coveredAd');
                                curFirstPlace = sumResult + parseInt(blockSettingArray[i]["elementStep"]) + 1;
                                curElementCount--;
                                repeatableSuccess = true;
                            } else {
                                repeatableSuccess = false;
                                break;
                            }
                        }
                    }
                    if (repeatableSuccess==true) {
                        usedBlockSettingArrayIds.push(block_number);
                        blockSettingArray.splice(i--, 1);
                        poolbackI = 1;
                        repeatableBlockIdentifier++;
                    } else {
                        if (!blockSettingArray[i]["unsuccess"]) {
                            blockSettingArray[i]["unsuccess"] = 1;
                        } else {
                            blockSettingArray[i]["unsuccess"] = Math.round(blockSettingArray[i]["unsuccess"] + 1);
                        }
                        if (blockSettingArray[i]["unsuccess"] > 10) {
                            usedBlockSettingArrayIds.push(block_number);
                            blockSettingArray.splice(i--, 1);
                            poolbackI = 1;
                        } else {
                            blockSettingArray[i]["firstPlace"] = curFirstPlace;
                            blockSettingArray[i]["elementCount"] = curElementCount;
                            blockSettingArray[i]["elementStep"] = curElementStep;
                            repeat = true;
                        }
                    }
                }
                else if (blockSettingArray[i]["setting_type"] == 3) {
                    let elementTypeSymbol = '';
                    let elementSpaceSymbol = '';
                    let elementName = '';
                    let elementType = '';
                    let elementTag  = '';
                    let findQuery = 0;
                    let directClassResult = [];
                    let directElement = blockSettingArray[i]["directElement"].trim();

                    if (directElement.search('#') > -1) {
                        findQuery = 1;
                    } else if ((directElement.search('#') < 0)&&(directElement.search('.') > -1)) {
                        directClassResult = directClassElementDetecting(blockSettingArray, directElement);
                        findQuery = directClassResult['findQuery'];
                        currentElement = directClassResult['currentElement'];
                    }
                    if (findQuery == 1) {
                        currentElement = document.querySelector(directElement);
                    }
                    if (currentElement) {
                        currentElementChecker = true;
                    }

                    if (currentElement != undefined && currentElement != null && currentElementChecker) {
                        posCurrentElement = initTargetToInsert(blockSettingArray[i]["elementPosition"], 'element', currentElement);
                        currentElement.parentNode.insertBefore(elementToAdd, posCurrentElement);
                        elementToAdd.classList.remove('coveredAd');
                        currentElement.classList.add('rbinder-'+binderName);
                        usedBlockSettingArrayIds.push(block_number);
                        blockSettingArray.splice(i--, 1);
                        poolbackI = 1;
                    } else {
                        repeat = true;
                    }
                }
                else if (blockSettingArray[i]["setting_type"] == 4) {
                    document.querySelector("#content_pointer_id").parentElement.append(elementToAdd);
                    usedBlockSettingArrayIds.push(block_number);
                    blockSettingArray.splice(i--, 1);
                    poolbackI = 1;
                }
                else if (blockSettingArray[i]["setting_type"] == 5) {
                    let currentElementList = cureentElementsGather('p', 1, content_pointer.parentElement);
                    if (currentElementList&&currentElementList.length > 0) {
                        let pCount = currentElementList.length;
                        let elementNumber = Math.round(pCount/2);
                        if (pCount > 1) {
                            currentElement = currentElementList[elementNumber+1];
                        }
                        if (currentElement != undefined && currentElement != null) {
                            if (pCount > 1) {
                                currentElement.parentNode.insertBefore(elementToAdd, currentElement);
                            } else {
                                currentElement.parentNode.insertBefore(elementToAdd, currentElement.nextSibling);
                            }
                            elementToAdd.classList.remove('coveredAd');
                            currentElement.classList.add('rbinder-'+binderName);
                            usedBlockSettingArrayIds.push(block_number);
                            blockSettingArray.splice(i--, 1);
                            poolbackI = 1;
                        } else {
                            repeat = true;
                        }
                    } else {
                        repeat = true;
                    }
                }
                else if (blockSettingArray[i]["setting_type"] == 6) {
                    if (containerFor6th.length > 0) {
                        for (let j = 0; j < containerFor6th.length; j++) {
                            if (containerFor6th[j]["elementPlace"]<blockSettingArray[i]["elementPlace"]) {
                                /* continue; */
                                if (j == containerFor6th.length-1) {
                                    containerFor6th.push(blockSettingArray[i]);
                                    /* usedAdBlocksArray.push(checkIfBlockUsed); */
                                    usedBlockSettingArrayIds.push(block_number);
                                    blockSettingArray.splice(i--, 1);
                                    poolbackI = 1;
                                    break;
                                }
                            } else {
                                for (let k = containerFor6th.length-1; k > j-1; k--) {
                                    containerFor6th[k + 1] = containerFor6th[k];
                                }
                                containerFor6th[j] = blockSettingArray[i];
                                /* usedAdBlocksArray.push(checkIfBlockUsed); */
                                usedBlockSettingArrayIds.push(block_number);
                                blockSettingArray.splice(i--, 1);
                                poolbackI = 1;
                                break;
                            }
                        }
                    } else {
                        containerFor6th.push(blockSettingArray[i]);
                        usedBlockSettingArrayIds.push(block_number);
                        blockSettingArray.splice(i--, 1);
                        poolbackI = 1;
                    }
                /* vidpravutu v vidstiinuk dlya 6ho tipa */
                }
                else if (blockSettingArray[i]["setting_type"] == 7) {
                    if (containerFor7th.length > 0) {
                        for (let j = 0; j < containerFor7th.length; j++) {
                            if (containerFor7th[j]["elementPlace"]<blockSettingArray[i]["elementPlace"]) {
                                /* continue; */
                                if (j == containerFor7th.length-1) {
                                    containerFor7th.push(blockSettingArray[i]);
                                    usedBlockSettingArrayIds.push(block_number);
                                    blockSettingArray.splice(i--, 1);
                                    poolbackI = 1;
                                    break;
                                }
                            } else {
                                for (let k = containerFor7th.length-1; k > j-1; k--) {
                                    containerFor7th[k + 1] = containerFor7th[k];
                                }
                                containerFor7th[j] = blockSettingArray[i];
                                usedBlockSettingArrayIds.push(block_number);
                                blockSettingArray.splice(i--, 1);
                                poolbackI = 1;
                                break;
                            }
                        }
                    } else {
                        containerFor7th.push(blockSettingArray[i]);
                        usedBlockSettingArrayIds.push(block_number);
                        blockSettingArray.splice(i--, 1);
                        poolbackI = 1;
                    }
                /* vidpravutu v vidstiinuk dlya 7ho tipa */
                }
            } catch (e) {
                console.log(e.message);
            }
        }

        var array = textLengthGatherer(lordOfElements),
            tlArray = array.array,
            length = array.length;

        if (containerFor6th.length > 0) {
            percentInserter(lordOfElements, containerFor6th, tlArray, length);
        }
        if (containerFor7th.length > 0) {
            symbolInserter(lordOfElements, containerFor7th, tlArray);
        }
        shortcodesInsert();
        let stopper = 0;

        window.addEventListener('load', function () {
            if (repeat = true) {
                setTimeout(function () {
                    /* asyncBlocksInsertingFunction(blockSettingArray, contentLength) */
                    asyncBlocksInsertingFunction(blockSettingArray);
                }, 100);
            }
        });
    } catch (e) {
        console.log(e.message);
    }
}

function possibleTagsInCheckConfirmer(possibleTagsArray, possibleTagsInCheck) {
    if (possibleTagsArray.includes("LI")) {
        if (possibleTagsArray.includes("UL")) {
            possibleTagsInCheck.push("UL");
        }
        if (possibleTagsArray.includes("OL")) {
            possibleTagsInCheck.push("OL");
        }
    }

    return false;
}

function textLengthGatherer(lordOfElementsLoc) {
    var possibleTagsArray;
    if (typeof tagsListForTextLength!=="undefined") {
        possibleTagsArray = tagsListForTextLength;
    } else {
        possibleTagsArray = ["P", "H1", "H2", "H3", "H4", "H5", "H6", "DIV", "BLOCKQUOTE", "INDEX", "ARTICLE", "SECTION"];
    }
    let possibleTagsInCheck = ["DIV", "INDEX", "SECTION"];

    possibleTagsInCheckConfirmer(possibleTagsArray, possibleTagsInCheck);
    let excArr = excIdClUnpacker(),
        textLength = 0,
        tlArray = [];

    function textLengthGathererRec(lordOfElementsLoc) {
        let allowed;
        let cou1;
        let classesArray;
        let countSuccess = 0;
        try {
            for (let i = 0; i < lordOfElementsLoc.children.length; i++) {
                if (possibleTagsArray.includes(lordOfElementsLoc.children[i].tagName)
                    &&!lordOfElementsLoc.children[i].classList.contains("percentPointerClass")
                    &&lordOfElementsLoc.children[i].id!="toc_container"
                ) {
                    if (possibleTagsInCheck.includes(lordOfElementsLoc.children[i].tagName)
                        &&(lordOfElementsLoc.children[i].children.length > 0)
                    ) {
                        allowed = true;
                        if (lordOfElementsLoc.children[i].id&&excArr['id'].length > 0) {
                            cou1 = 0;
                            while (excArr['id'][cou1]) {
                                if (lordOfElementsLoc.children[i].id.toLowerCase()==excArr['id'][cou1].toLowerCase()) {
                                    allowed = false;
                                    break;
                                }
                                cou1++;
                            }
                        }

                        if (lordOfElementsLoc.children[i].classList.length > 0&&excArr['class'].length > 0) {
                            cou1 = 0;
                            while (excArr['class'][cou1]) {
                                classesArray = excArr['class'][cou1].split('.');
                                if (classesArray.every(className => lordOfElementsLoc.children[i].classList.contains(className))) {
                                    allowed = false;
                                    break;
                                }
                                cou1++;
                            }
                        }

                        if (excArr['tag'].length > 0) {
                            cou1 = 0;
                            while (excArr['tag'][cou1]) {
                                if (lordOfElementsLoc.children[i].tagName.toLowerCase()==excArr['tag'][cou1].toLowerCase()) {
                                    allowed = false;
                                    break;
                                }
                                cou1++;
                            }
                        }

                        if (allowed) {
                            if (textLengthGathererRec(lordOfElementsLoc.children[i], excArr, possibleTagsArray, possibleTagsInCheck)) {
                                countSuccess++;
                                continue;
                            }
                        }
                    }
                    textLength = textLength + lordOfElementsLoc.children[i].innerText.length;
                    tlArray.push({
                        tag: lordOfElementsLoc.children[i].tagName,
                        length: lordOfElementsLoc.children[i].innerText.length,
                        lengthSum: textLength,
                        element: lordOfElementsLoc.children[i]
                    });
                    countSuccess++;
                }
            }
        } catch (er) {
            console.log(er.message);
        }
        return countSuccess > 0;
    }

    textLengthGathererRec(lordOfElementsLoc);

    return {array: tlArray, length: textLength};
}

window.asyncFunctionLauncher = function() {
    if (window.jsInputerLaunch !== undefined
        &&[15, 10].includes(window.jsInputerLaunch)
        &&(typeof asyncBlocksInsertingFunction !== 'undefined' )
        &&(typeof asyncBlocksInsertingFunction === 'function')
        &&typeof endedSc!=='undefined'&&
        typeof endedCc!=='undefined'&&
        typeof usedAdBlocksArray!=='undefined'&&
        typeof usedBlockSettingArrayIds!=='undefined'&&
        typeof sameElementAfterWidth!=='undefined'&&
        typeof sameElementAfterExcClassId!=='undefined'&&
        typeof sameElementAfterFromConstruction!=='undefined'&&
        typeof rb_tempElement_check!=='undefined'&&
        typeof rb_tempElement!=='undefined'&&
        typeof window.jsInputerLaunch!=='undefined') {
        /* asyncBlocksInsertingFunction(blockSettingArray, contentLength); */
        asyncBlocksInsertingFunction(blockSettingArray);
        if (!endedSc) {
            shortcodesInsert();
        }
        if (!endedCc) {
            /* clearUnsuitableCache(0); */
        }
        /* blocksReposition();
        cachePlacing();
        symbolMarkersPlaced(); */
    } else {
        setTimeout(function () {
            asyncFunctionLauncher();
        }, 50);
    }
};
/* asyncFunctionLauncher(); */

function asyncInsertingsInsertingFunction(insertingsArray) {
    let currentElementForInserting = 0;
    let currentElementToMove = 0;
    let positionElement = 0;
    let position = 0;
    let insertToAdd = 0;
    let postId = 0;
    let repeatSearch = 0;
    if (insertingsArray&&insertingsArray.length > 0) {
        for (let i = 0; i < insertingsArray.length; i++) {
            if (!insertingsArray[i]['used']||(insertingsArray[i]['used']&&insertingsArray[i]['used']==0)) {
                positionElement = insertingsArray[i]['position_element'];
                position = insertingsArray[i]['position'];
                insertToAdd = insertingsArray[i]['content'];
                postId = insertingsArray[i]['postId'];

                currentElementForInserting = document.querySelector(positionElement);

                currentElementToMove = document.querySelector('.coveredInsertings[data-id="'+postId+'"]');
                if (currentElementForInserting) {
                    if (position==0) {
                        currentElementForInserting.parentNode.insertBefore(currentElementToMove, currentElementForInserting);
                        currentElementToMove.classList.remove('coveredInsertings');
                        insertingsArray[i]['used'] = 1;
                    } else {
                        currentElementForInserting.parentNode.insertBefore(currentElementToMove, currentElementForInserting.nextSibling);
                        currentElementToMove.classList.remove('coveredInsertings');
                        insertingsArray[i]['used'] = 1;
                    }
                } else {
                    repeatSearch = 1;
                }
            }
        }
    }
    if (repeatSearch == 1) {
        setTimeout(function () {
            asyncInsertingsInsertingFunction(insertingsArray);
        }, 100)
    }
}

function insertingsFunctionLaunch() {
    if (window.jsInsertingsLaunch !== undefined&&jsInsertingsLaunch == 25) {
        asyncInsertingsInsertingFunction(insertingsArray);
    } else {
        setTimeout(function () {
            insertingsFunctionLaunch();
        }, 100)
    }
}

function setLongCache() {
    let xhttp = new XMLHttpRequest();
    let sendData = 'action=setLongCache&type=longCatching';
    xhttp.onreadystatechange = function(redata) {
        if (this.readyState == 4 && this.status == 200) {
            console.log('long cache deployed');
        }
    };
    xhttp.open("POST", rb_ajaxurl, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(sendData);
}

function cachePlacing(alert_type, errorInfo=null) {
    let adBlocks = document.querySelectorAll('.percentPointerClass .' + block_classes.join(', .percentPointerClass .'));
    let curAdBlock;
    let okStates = ['done','refresh-wait','no-block','fetched'];
    /* let adId = -1; */
    let blockAid = null;
    let blockId;

    if (typeof cachedBlocksArray !== 'undefined'&&cachedBlocksArray&&cachedBlocksArray.length > 0&&adBlocks&&adBlocks.length > 0) {
        for (let i = 0; i < adBlocks.length; i++) {
            blockAid = adBlocks[i]['dataset']['aid'];

            if (!blockAid) {
                blockId = adBlocks[i]['dataset']['id'];
                if (cachedBlocksArray[blockId]) {
                    jQuery(adBlocks[i]).html(cachedBlocksArray[blockId]);
                }
            }
        }
    }

    if (alert_type&&alert_type=='high') {
        setLongCache();
    }
}

function symbolInserter(lordOfElements, containerFor7th, tlArray) {
    try {
        var currentChildrenLength = 0;
        let previousBreak = 0;
        let needleLength;
        let currentSumLength;
        let elementToAdd;
        let elementToBind;
        let elementToAddStyle;
        let block_number;
        let binderName;

        if (!document.getElementById("markedSpan1")) {
            for (let i = 0; i < containerFor7th.length; i++) {
                previousBreak = 0;
                currentChildrenLength = 0;
                currentSumLength = 0;
                needleLength = Math.abs(containerFor7th[i]['elementPlace']);
                binderName = elementBinderNameGenerator();

                elementToAdd = document.createElement("div");
                elementToAdd.classList.add("percentPointerClass");
                elementToAdd.classList.add("marked");
                if (containerFor7th[i]["sc"]==1) {
                    elementToAdd.classList.add("scMark");
                }
                elementToAdd.dataset.rbinder = binderName;
                elementToAdd.innerHTML = containerFor7th[i]["text"];
                block_number = elementToAdd.children[0].attributes['data-id'].value;
                if (!elementToAdd) {
                    continue;
                }

                elementToAddStyle = createStyleElement(block_number, containerFor7th[i]["elementCss"]);

                if (elementToAddStyle&&elementToAddStyle!='default') {
                    elementToAdd.style.textAlign = elementToAddStyle;
                }

                if (containerFor7th[i]['elementPlace'] < 0) {
                    for (let j = tlArray.length-1; j > -1; j--) {
                        currentSumLength = currentSumLength + tlArray[j]['length'];
                        if (needleLength < currentSumLength) {
                            elementToBind = tlArray[j]['element'];
                            elementToBind = currentElementReceiverSpec(true, j, tlArray, elementToBind);
                            elementToBind.parentNode.insertBefore(elementToAdd, elementToBind);
                            elementToBind.classList.add('rbinder-'+binderName);
                            elementToAdd.classList.remove('coveredAd');
                            break;
                        }
                    }
                } else if (containerFor7th[i]['elementPlace'] == 0) {
                    elementToBind = tlArray[0]['element'];
                    elementToBind.parentNode.insertBefore(elementToAdd, elementToBind);
                    elementToBind.classList.add('rbinder-'+binderName);
                    elementToAdd.classList.remove('coveredAd');
                } else {
                    for (let j = 0; j < tlArray.length; j++) {
                        currentSumLength = currentSumLength + tlArray[j]['length'];
                        if (needleLength < currentSumLength) {
                            elementToBind = tlArray[j]['element'];
                            elementToBind = currentElementReceiverSpec(false, j, tlArray, elementToBind);
                            elementToBind.parentNode.insertBefore(elementToAdd, elementToBind.nextSibling);
                            elementToBind.classList.add('rbinder-'+binderName);
                            elementToAdd.classList.remove('coveredAd');
                            break;
                        }
                    }
                }
            }

            var spanMarker = document.createElement("span");
            spanMarker.setAttribute("id", "markedSpan1");
            lordOfElements.prepend(spanMarker);
        }
    } catch (e) {
        console.log(e);
    }
}

function percentInserter(lordOfElements, containerFor6th, tlArray, textLength) {
    try {
        var textNeedyLength = 0;
        let elementToAdd;
        var elementToBind;
        let elementToAddStyle;
        let block_number;
        var binderName;
        /* var checkIfBlockUsed = 0; */

        function insertByPercents(textLength) {
            let localMiddleValue = 0;

            for (let j = 0; j < containerFor6th.length; j++) {
                textNeedyLength = Math.round(textLength * (containerFor6th[j]["elementPlace"]/100));
                for (let i = 0; i < tlArray.length; i++) {
                    if (tlArray[i]['lengthSum'] >= textNeedyLength) {
                        binderName = elementBinderNameGenerator();

                        elementToAdd = document.createElement("div");
                        elementToAdd.classList.add("percentPointerClass");
                        elementToAdd.classList.add("marked");
                        if (containerFor6th[j]["sc"]==1) {
                            elementToAdd.classList.add("scMark");
                        }
                        elementToAdd.dataset.rbinder = binderName;
                        elementToAdd.innerHTML = containerFor6th[j]["text"];
                        if (!elementToAdd) {
                            break;
                        }
                        block_number = elementToAdd.children[0].attributes['data-id'].value;
                        elementToAddStyle = createStyleElement(block_number, containerFor6th[j]["elementCss"]);
                        if (elementToAddStyle&&elementToAddStyle!='default') {
                            elementToAdd.style.textAlign = elementToAddStyle;
                        }

                        localMiddleValue = tlArray[i]['lengthSum'] - Math.round(tlArray[i]['length']/2);
                        elementToBind = tlArray[i]['element'];
                        currentElementReceiverSpec(false, i, tlArray, elementToBind);
                        if (textNeedyLength < localMiddleValue) {
                            elementToBind.parentNode.insertBefore(elementToAdd, elementToBind);
                        } else {
                            elementToBind.parentNode.insertBefore(elementToAdd, elementToBind.nextSibling);
                        }
                        elementToBind.classList.add('rbinder-'+binderName);
                        elementToAdd.classList.remove('coveredAd');
                        break;
                    }
                }
            }
            return false;
        }

        function clearTlMarks() {
            let marksForDeleting = document.querySelectorAll('.textLengthMarker');

            if (marksForDeleting.length > 0) {
                for (let i = 0; i < marksForDeleting.length; i++) {
                    marksForDeleting[i].remove();
                }
            }
        }

        if (!document.getElementById("markedSpan")) {
            insertByPercents(textLength);
            clearTlMarks();
            var spanMarker = document.createElement("span");
            spanMarker.setAttribute("id", "markedSpan");
            lordOfElements.prepend(spanMarker);
        }
    } catch (e) {
        console.log(e.message);
    }
}

function saveContentBlock(contentContainer) {
    try {
        if (!gather_content) {
            console.log('content gather save function entered');
            let xhttp = new XMLHttpRequest();
            let sendData = 'action=RFWP_saveContentContainer&type=gatherContentBlock&data='+contentContainer;
            xhttp.onreadystatechange = function(redata) {
                if (this.readyState == 4 && this.status == 200) {
                    console.log('content gather succeed');
                } else {
                    console.log('content gather gone wrong');
                }
            };
            xhttp.open("POST", rb_ajaxurl, true);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send(sendData);
        }
    } catch (er) {
        console.log('content gather error: '+er+';');
    }
}

window.gatherContentBlock = function() {
    let cPointer = null,
        cPointerParent = null,
        cPointerParentString = null,
        classWords = ['content','entry','post','wrap','description','taxonomy'],
        classChoosed = false;

    cPointer =  document.querySelector('#content_pointer_id');
    if (cPointer) {
        if (window.jsInputerLaunch!==15) {
            return false;
        }
        cPointerParent = cPointer.parentElement;
        if (cPointerParent) {
            if (cPointerParent.id) {
                cPointerParentString = '#'+cPointerParent.id;
            } else {
                if (cPointerParent.classList.length > 0) {
                    cPointerParentString = '.'+cPointerParent.classList[0];
                    for (let j = 0; j < classWords.length; j++) {
                        for (let i = 0; i < cPointerParent.classList.length; i++) {
                            if (cPointerParent.classList[i].includes(classWords[j])) {
                                cPointerParentString = '.'+cPointerParent.classList[i];
                                classChoosed = true;
                                break;
                            }
                        }
                        if (classChoosed===true) {
                            break;
                        }
                    }
                }
            }
            if (cPointerParentString) {
                console.log('content gather content block detected');
                /* cPointerParentString = JSON.stringify(cPointerParentString); */
                saveContentBlock(cPointerParentString);
            }
        }
    } else {
        console.log('content gather delayed');
        setTimeout(function () {
            gatherContentBlock();
        }, 500);
    }
};

window.removeMarginClass = function(blockObject) {
    if (blockObject && typeof window.jsInputerLaunch !== 'undefined' && [15, 10].includes(window.jsInputerLaunch)) {
        let binderName,
            neededElement,
            currentDirection,
            seekerIterationCount,
            currentSubling;

        binderName = blockObject.dataset.rbinder;
        if (binderName) {
            seekerIterationCount = 0;
            currentDirection = 'before';
            do {
                seekerIterationCount++;
                currentSubling = blockObject.nextElementSibling;
                if (currentSubling&&currentSubling.classList.contains('rbinder-'+binderName)) {
                    neededElement = currentSubling;
                }
            } while (currentSubling&&!neededElement&&seekerIterationCount < 5);

            if (!neededElement) {
                seekerIterationCount = 0;
                currentDirection = 'after';
                do {
                    seekerIterationCount++;
                    currentSubling = blockObject.previousElementSibling;
                    if (currentSubling&&currentSubling.classList.contains('rbinder-'+binderName)) {
                        neededElement = currentSubling;
                    }
                } while (currentSubling&&!neededElement&&seekerIterationCount < 5);
            }
            if (neededElement) {
                if (currentDirection === 'before') {
                    neededElement.classList.remove('rfwp_removedMarginTop');
                } else {
                    neededElement.classList.remove('rfwp_removedMarginBottom');
                }
            }
        }
    }

    return false;
};

function elementBinderNameGenerator() {
    let binderName = '',
        checkedElements,
        passed = false;

    while (passed===false) {
        binderName = Math.floor(Math.random()*100000);
        checkedElements = document.querySelectorAll('[data-rbinder="'+binderName+'"]');
        if (checkedElements.length < 1) {
            passed = true;
        }
    }

    return binderName;
}
</script>
<script>
if (typeof rb_ajaxurl==='undefined') {var rb_ajaxurl = 'https://pythonpip.ru/wp-admin/admin-ajax.php';}
if (typeof cache_devices==='undefined') {var cache_devices = true;}
var nReadyBlock = false;
var fetchedCounter = 0;

function sendReadyBlocksNew(blocks) {
    if (!cache_devices) {
        let xhttp = new XMLHttpRequest();
        let sendData = 'action=saveAdBlocks&type=blocksGethering&data='+blocks;
        xhttp.onreadystatechange = function(redata) {
            if (this.readyState == 4 && this.status == 200) {
                console.log('cache succeed');
            }
        };
        xhttp.open("POST", rb_ajaxurl, true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send(sendData);
    }
}

function gatherReadyBlocks() {
    if (block_classes && block_classes.length) {
        let blocks = {};
        let counter1 = 0;
        let gatheredBlocks = document.querySelectorAll('.' + block_classes.join(', .'));
        let checker = 0;
        let adContent = '';
        let curState = '';
        let thisData = [];
        let sumData = [];
        let newBlocks = '';
        let thisDataString = '';

        if (gatheredBlocks.length > 0) {
            blocks.data = {};

            for (let i = 0; i < gatheredBlocks.length; i++) {
                curState = gatheredBlocks[i]['dataset']["state"].toLowerCase();
                checker = 0;
                if (curState&&gatheredBlocks[i]['innerHTML'].length > 0&&gatheredBlocks[i]['dataset']['aid'] > 0&&curState!='no-block') {
                    if (gatheredBlocks[i]['innerHTML'].length > 0) {
                        checker = 1;
                    }
                    if (checker==1) {
                        blocks.data[counter1] = {id:gatheredBlocks[i]['dataset']['id'],code:gatheredBlocks[i]['dataset']['aid']};
                        counter1++;
                    }
                }
            }

            blocks = JSON.stringify(blocks);
            sendReadyBlocksNew(blocks);
        }
    } else nReadyBlock = true;
}

function timeBeforeGathering() {
    if (block_classes && block_classes.length > 0)
    {
        let gatheredBlocks = document.querySelectorAll('.' + block_classes.join(', .'));
        let okStates = ['done','refresh-wait','no-block','fetched'];
        let curState = '';

        for (let i = 0; i < gatheredBlocks.length; i++) {
            if (!gatheredBlocks[i]['dataset']["state"]) {
                nReadyBlock = true;
                break;
            } else {
                curState = gatheredBlocks[i]['dataset']["state"].toLowerCase();
                if (!okStates.includes(curState)) {
                    nReadyBlock = true;
                    break;
                } else if (curState=='fetched'&&fetchedCounter < 3) {
                    fetchedCounter++;
                    nReadyBlock = true;
                    break;
                }
            }
        }
    }
    else nReadyBlock = true;

    if (nReadyBlock == true) {
        nReadyBlock = false;
        setTimeout(timeBeforeGathering,2000);
    } else {
        gatherReadyBlocks();
    }
}

function launchTimeBeforeGathering() {
    if (document.readyState === "complete" || (document.readyState !== "loading" && !document.documentElement.doScroll)) {
        timeBeforeGathering();
    } else {
        setTimeout(launchTimeBeforeGathering,100);
    }
}
launchTimeBeforeGathering();

</script>

<style type='text/css'>

#wallpaper {
	background: url() no-repeat 50% 0;
	}
body,
.blog-widget-text p,
.feat-widget-text p,
.post-info-right,
span.post-excerpt,
span.feat-caption,
span.soc-count-text,
#content-main p,
#commentspopup .comments-pop,
.archive-list-text p,
.author-box-bot p,
#post-404 p,
.foot-widget,
#home-feat-text p,
.feat-top2-left-text p,
.feat-wide1-text p,
.feat-wide4-text p,
#content-main table,
.foot-copy p,
.video-main-text p {
	font-family: 'Montserrat', sans-serif;
	}

a,
a:visited,
.post-info-name a {
	color: #7289DA;
	}

a:hover {
	color: #999999;
	}

.fly-but-wrap,
span.feat-cat,
span.post-head-cat,
.prev-next-text a,
.prev-next-text a:visited,
.prev-next-text a:hover {
	background: #7289DA;
	}

.fly-but-wrap {
	background: #eb0254;
	}

.fly-but-wrap span {
	background: #ffffff;
	}



span.post-header {
	border-top: 4px solid #7289DA;
	}

#main-nav-wrap,
nav.main-menu-wrap,
.nav-logo,
.nav-right-wrap,
.nav-menu-out,
.nav-logo-out,
#head-main-top {
	-webkit-backface-visibility: hidden;
	background: #eb0254;
	}

nav.main-menu-wrap ul li a,
.nav-menu-out:hover ul li:hover a,
.nav-menu-out:hover span.nav-search-but:hover i,
.nav-menu-out:hover span.nav-soc-but:hover i,
span.nav-search-but i,
span.nav-soc-but i {
	color: #ffffff;
	}

.nav-menu-out:hover li.menu-item-has-children:hover a:after,
nav.main-menu-wrap ul li.menu-item-has-children a:after {
	border-color: #ffffff transparent transparent transparent;
	}

.nav-menu-out:hover ul li a,
.nav-menu-out:hover span.nav-search-but i,
.nav-menu-out:hover span.nav-soc-but i {
	color: #fdacc8;
	}

.nav-menu-out:hover li.menu-item-has-children a:after {
	border-color: #fdacc8 transparent transparent transparent;
	}

.nav-menu-out:hover ul li ul.mega-list li a,
.side-list-text p,
.row-widget-text p,
.blog-widget-text h2,
.feat-widget-text h2,
.archive-list-text h2,
h2.author-list-head a,
.mvp-related-text a {
	color: #222222;
	}

ul.mega-list li:hover a,
ul.side-list li:hover .side-list-text p,
ul.row-widget-list li:hover .row-widget-text p,
ul.blog-widget-list li:hover .blog-widget-text h2,
.feat-widget-wrap:hover .feat-widget-text h2,
ul.archive-list li:hover .archive-list-text h2,
ul.archive-col-list li:hover .archive-list-text h2,
h2.author-list-head a:hover,
.mvp-related-posts ul li:hover .mvp-related-text a {
	color: #999999 !important;
	}

span.more-posts-text,
a.inf-more-but,
#comments-button a,
#comments-button span.comment-but-text {
	border: 1px solid #7289DA;
	}

span.more-posts-text,
a.inf-more-but,
#comments-button a,
#comments-button span.comment-but-text {
	color: #7289DA !important;
	}

#comments-button a:hover,
#comments-button span.comment-but-text:hover,
a.inf-more-but:hover,
span.more-posts-text:hover {
	background: #7289DA;
	}

nav.main-menu-wrap ul li a,
ul.col-tabs li a,
nav.fly-nav-menu ul li a,
.foot-menu .menu li a {
	font-family: 'Montserrat', sans-serif;
	}

.feat-top2-right-text h2,
.side-list-text p,
.side-full-text p,
.row-widget-text p,
.feat-widget-text h2,
.blog-widget-text h2,
.prev-next-text a,
.prev-next-text a:visited,
.prev-next-text a:hover,
span.post-header,
.archive-list-text h2,
#woo-content h1.page-title,
.woocommerce div.product .product_title,
.woocommerce ul.products li.product h3,
.video-main-text h2,
.mvp-related-text a {
	font-family: 'Montserrat', sans-serif;
	}

.feat-wide-sub-text h2,
#home-feat-text h2,
.feat-top2-left-text h2,
.feat-wide1-text h2,
.feat-wide4-text h2,
.feat-wide5-text h2,
h1.post-title,
#content-main h1.post-title,
#post-404 h1,
h1.post-title-wide,
#content-main blockquote p,
#commentspopup #content-main h1 {
	font-family: 'Montserrat', sans-serif;
	}

h3.home-feat-title,
h3.side-list-title,
#infscr-loading,
.score-nav-menu select,
h1.cat-head,
h1.arch-head,
h2.author-list-head,
h3.foot-head,
#content-main h1,
#content-main h2,
#content-main h3,
#content-main h4,
#content-main h5,
#content-main h6 {
	font-family: 'Montserrat', sans-serif;
	}

</style>
	
<style type="text/css">


.post-cont-out,
.post-cont-in {
	margin-right: 0;
	}

.nav-links {
	display: none;
	}







	

</style>

			<style>
			#related_posts_thumbnails li{
				border-right: 1px solid #dddddd;
				background-color: #ffffff			}
			#related_posts_thumbnails li:hover{
				background-color: #eeeeee;
			}
			.relpost_content{
				font-size:	18px;
				color: 		#333333;
			}
			.relpost-block-single{
				background-color: #ffffff;
				border-right: 1px solid  #dddddd;
				border-left: 1px solid  #dddddd;
				margin-right: -1px;
			}
			.relpost-block-single:hover{
				background-color: #eeeeee;
			}
		</style>

	

<style>
    .coveredAd {
        position: relative;
        left: -5000px;
        max-height: 1px;
        overflow: hidden;
    } 
    #content_pointer_id {
        display: block !important;
        width: 100% !important;
    }
    .rfwp_removedMarginTop {
        margin-top: 0 !important;
    }
    .rfwp_removedMarginBottom {
        margin-bottom: 0 !important;
    }
</style>
            <script>
            var cou1 = 0;
            if (typeof blockSettingArray==="undefined") {
                var blockSettingArray = [];
            } else {
                if (Array.isArray(blockSettingArray)) {
                    cou1 = blockSettingArray.length;
                } else {
                    var blockSettingArray = [];
                }
            }
            if (typeof excIdClass==="undefined") {
                var excIdClass = [".percentPointerClass",".content_rb",".cnt32_rl_bg_str",".rl_cnt_bg",".addedInserting","#toc_container","table","blockquote"];
            }
            if (typeof blockDuplicate==="undefined") {
                var blockDuplicate = "yes";
            }                        
            if (typeof obligatoryMargin==="undefined") {
                var obligatoryMargin = 1;
            }
            
            if (typeof tagsListForTextLength==="undefined") {
                var tagsListForTextLength = ["P","H1","H2","H3","H4","H5","H6","DIV","BLOCKQUOTE","INDEX","ARTICLE","SECTION"];
            }                        
            blockSettingArray[cou1] = [];
blockSettingArray[cou1]["minSymbols"] = 0;
blockSettingArray[cou1]["maxSymbols"] = 0;
blockSettingArray[cou1]["minHeaders"] = 0;
blockSettingArray[cou1]["maxHeaders"] = 0;
blockSettingArray[cou1]["id"] = '89'; 
blockSettingArray[cou1]["sc"] = '0'; 
blockSettingArray[cou1]["text"] = '<div class=\"rl_cnt_bg\" data-id=\"292816\"></div>'; 
blockSettingArray[cou1]["setting_type"] = 4; 
blockSettingArray[cou1]["elementCss"] = "center"; 
cou1++;
blockSettingArray[cou1] = [];
blockSettingArray[cou1]["minSymbols"] = 0;
blockSettingArray[cou1]["maxSymbols"] = 0;
blockSettingArray[cou1]["minHeaders"] = 0;
blockSettingArray[cou1]["maxHeaders"] = 0;
blockSettingArray[cou1]["id"] = '90'; 
blockSettingArray[cou1]["sc"] = '0'; 
blockSettingArray[cou1]["text"] = '<div class=\"rl_cnt_bg\" data-id=\"270693\"></div>'; 
blockSettingArray[cou1]["setting_type"] = 4; 
blockSettingArray[cou1]["elementCss"] = "default"; 
cou1++;
blockSettingArray[cou1] = [];
blockSettingArray[cou1]["minSymbols"] = 0;
blockSettingArray[cou1]["maxSymbols"] = 0;
blockSettingArray[cou1]["minHeaders"] = 0;
blockSettingArray[cou1]["maxHeaders"] = 0;
blockSettingArray[cou1]["id"] = '91'; 
blockSettingArray[cou1]["sc"] = '0'; 
blockSettingArray[cou1]["text"] = '<div class=\"rl_cnt_bg\" data-id=\"270692\"></div>'; 
blockSettingArray[cou1]["setting_type"] = 1; 
blockSettingArray[cou1]["elementCss"] = "default"; 
blockSettingArray[cou1]["element"] = "p"; 
blockSettingArray[cou1]["elementPosition"] = 1; 
blockSettingArray[cou1]["elementPlace"] = 18; 
cou1++;
blockSettingArray[cou1] = [];
blockSettingArray[cou1]["minSymbols"] = 0;
blockSettingArray[cou1]["maxSymbols"] = 0;
blockSettingArray[cou1]["minHeaders"] = 0;
blockSettingArray[cou1]["maxHeaders"] = 0;
blockSettingArray[cou1]["id"] = '92'; 
blockSettingArray[cou1]["sc"] = '0'; 
blockSettingArray[cou1]["text"] = '<div class=\"rl_cnt_bg\" data-id=\"270691\"></div>'; 
blockSettingArray[cou1]["setting_type"] = 1; 
blockSettingArray[cou1]["elementCss"] = "default"; 
blockSettingArray[cou1]["element"] = "p"; 
blockSettingArray[cou1]["elementPosition"] = 1; 
blockSettingArray[cou1]["elementPlace"] = 12; 
cou1++;
blockSettingArray[cou1] = [];
blockSettingArray[cou1]["minSymbols"] = 0;
blockSettingArray[cou1]["maxSymbols"] = 0;
blockSettingArray[cou1]["minHeaders"] = 0;
blockSettingArray[cou1]["maxHeaders"] = 0;
blockSettingArray[cou1]["id"] = '93'; 
blockSettingArray[cou1]["sc"] = '0'; 
blockSettingArray[cou1]["text"] = '<div class=\"rl_cnt_bg\" data-id=\"270690\"></div>'; 
blockSettingArray[cou1]["setting_type"] = 1; 
blockSettingArray[cou1]["elementCss"] = "default"; 
blockSettingArray[cou1]["element"] = "p"; 
blockSettingArray[cou1]["elementPosition"] = 1; 
blockSettingArray[cou1]["elementPlace"] = 6; 
cou1++;
blockSettingArray[cou1] = [];
blockSettingArray[cou1]["minSymbols"] = 0;
blockSettingArray[cou1]["maxSymbols"] = 0;
blockSettingArray[cou1]["minHeaders"] = 0;
blockSettingArray[cou1]["maxHeaders"] = 0;
blockSettingArray[cou1]["id"] = '94'; 
blockSettingArray[cou1]["sc"] = '0'; 
blockSettingArray[cou1]["text"] = '<div class=\"rl_cnt_bg\" data-id=\"270687\"></div>'; 
blockSettingArray[cou1]["setting_type"] = 1; 
blockSettingArray[cou1]["elementCss"] = "default"; 
blockSettingArray[cou1]["element"] = "p"; 
blockSettingArray[cou1]["elementPosition"] = 1; 
blockSettingArray[cou1]["elementPlace"] = 1; 
cou1++;
console.log("bsa-l: "+blockSettingArray.length);
</script><script>
    if (typeof window.jsInputerLaunch === 'undefined') {
        window.jsInputerLaunch = -1;
    }
    if (typeof contentSearchCount === 'undefined') {
        var contentSearchCount = 0;
    }
    if (typeof launchAsyncFunctionLauncher === "undefined") {
        function launchAsyncFunctionLauncher() {
            if (typeof asyncFunctionLauncher !== "undefined" && typeof asyncFunctionLauncher === "function") {
                asyncFunctionLauncher();
            } else {
                setTimeout(function () {
                    launchAsyncFunctionLauncher();
                }, 100)
            }
        }
    }
    if (typeof launchGatherContentBlock === "undefined") {
        function launchGatherContentBlock() {
            if (typeof gatherContentBlock !== "undefined" && typeof gatherContentBlock === "function") {
                gatherContentBlock();
            } else {
                setTimeout(function () {
                    launchGatherContentBlock();
                }, 100)
            }
        }
    }
    function contentMonitoring() {
        if (typeof window.jsInputerLaunch==='undefined'||(typeof window.jsInputerLaunch!=='undefined'&&window.jsInputerLaunch==-1)) {
            let possibleClasses = ['.taxonomy-description','.entry-content','.post-wrap','#blog-entries','.content','.archive-posts__item-text','.single-company_wrapper','.posts-container','.content-area','.post-listing','.td-category-description','.jeg_posts_wrap'];
            let deniedClasses = ['.percentPointerClass','.addedInserting','#toc_container'];
            let deniedString = "";
            let contentSelector = '#content-main';
            let contentCheck = null;
            if (contentSelector) {
                contentCheck = document.querySelector(contentSelector);
            }

            if (block_classes && block_classes.length > 0) {
                for (var i = 0; i < block_classes.length; i++) {
                    if (block_classes[i]) {
                        deniedClasses.push('.' + block_classes[i]);
                    }
                }
            }

            if (deniedClasses&&deniedClasses.length > 0) {
                for (let i = 0; i < deniedClasses.length; i++) {
                    deniedString += ":not("+deniedClasses[i]+")";
                }
            }
            
            if (!contentCheck) {
                for (let i = 0; i < possibleClasses.length; i++) {
                    contentCheck = document.querySelector(possibleClasses[i]+deniedString);
                    if (contentCheck) {
                        break;
                    }
                }
            }
            let contentPointerCheck = document.querySelector('#content_pointer_id');
            if (contentCheck&&!contentPointerCheck) {                
                console.log('content is here');
                let cpSpan = document.createElement('SPAN');
                cpSpan.setAttribute('id', 'content_pointer_id');
                cpSpan.classList.add('no-content');
                cpSpan.setAttribute('data-content-length', '0');
                cpSpan.setAttribute('data-accepted-blocks', '89,90,91,92,93,94');
                cpSpan.setAttribute('data-rejected-blocks', '0');
                window.jsInputerLaunch = 10;
                
                contentCheck.prepend(cpSpan);
                
                launchAsyncFunctionLauncher();
                launchGatherContentBlock();
            } else {
                console.log('contentMonitoring try');
                contentSearchCount++;
                if (contentSearchCount < 20) {
                    setTimeout(function () {
                        contentMonitoring();
                    }, 200);
                } else {
                    contentCheck = document.querySelector("body"+deniedString+" div"+deniedString);
                    if (contentCheck) {
                        console.log('content is here hard');
                        let cpSpan = document.createElement('SPAN');
                        cpSpan.setAttribute('id', 'content_pointer_id');
                        cpSpan.classList.add('no-content');
                        cpSpan.classList.add('hard-content');
                        cpSpan.setAttribute('data-content-length', '0');
                        cpSpan.setAttribute('data-accepted-blocks', '89,90,91,92,93,94');
                        cpSpan.setAttribute('data-rejected-blocks', '0');
                        window.jsInputerLaunch = 10;
                        
                        contentCheck.prepend(cpSpan);
                        launchAsyncFunctionLauncher();
                    }   
                }
            }
        } else {
            console.log('jsInputerLaunch is here');
            launchGatherContentBlock();
        }
    }
    contentMonitoring();
</script><script async src="https://yandex.ru/ads/system/header-bidding.js"></script>
<script type="text/javascript" src="https://ads.digitalcaramel.com/js/pythonpip.ru.js"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6959883099270890"
     crossorigin="anonymous"></script>
<!-- Yandex.RTB -->
<script>window.yaContextCb=window.yaContextCb||[]</script>
<script src="https://yandex.ru/ads/system/context.js" async></script>
</head>

<body class="post-template-default single single-post postid-1840 single-format-standard">
	<div id="site" class="left relative">
		<div id="site-wrap" class="left relative">
						<div id="fly-wrap">
	<div class="fly-wrap-out">
		<div class="fly-side-wrap">
			
		</div><!--fly-side-wrap-->
		<div class="fly-wrap-in">
			<div id="fly-menu-wrap">
				<nav class="fly-nav-menu left relative">
					<div class="menu-menyu2-container"><ul id="menu-menyu2" class="menu"><li id="menu-item-2153" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-2153"><a href="https://pythonpip.ru/osnovy">Основы Python</a></li>
<li id="menu-item-2154" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-2154"><a href="https://pythonpip.ru/examples">Примеры</a></li>
</ul></div>				</nav>
			</div><!--fly-menu-wrap-->
		</div><!--fly-wrap-in-->
	</div><!--fly-wrap-out-->
</div><!--fly-wrap-->			<div id="head-main-wrap" class="left relative">
				<div id="head-main-top" class="left relative">
																														</div><!--head-main-top-->
				<div id="main-nav-wrap">
					<div class="nav-out">
						<div class="nav-in">
							<div id="main-nav-cont" class="left" itemscope itemtype="http://schema.org/Organization">
								<div class="nav-logo-out">
									<div class="nav-left-wrap left relative">
										<div class="fly-but-wrap left relative">
											<span></span>
											<span></span>
											<span></span>
											<span></span>
										</div><!--fly-but-wrap-->
																					<div class="nav-logo left">
																									<a itemprop="url" href="https://pythonpip.ru/"><img itemprop="logo" src="https://pythonpip.ru/wp-content/uploads/logotip.png" alt="Python самоучитель для начинающих" data-rjs="2" class="logo-width" /></a>
																																					
																							</div><!--nav-logo-->
																			</div><!--nav-left-wrap-->
									<div class="nav-logo-in">
										<div class="nav-menu-out">
											<div class="nav-menu-in">
												<nav class="main-menu-wrap left">
													<div class="menu-menyu-container"><ul id="menu-menyu" class="menu"><li id="menu-item-1024" class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent menu-item-1024"><a href="https://pythonpip.ru/examples">Примеры</a></li>
<li id="menu-item-1253" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-1253"><a href="https://pythonpip.ru/osnovy">Основы</a></li>
<li id="menu-item-2148" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2148"><a href="https://pythonpip.ru/tag/matplotlib">Matplotlib</a></li>
<li id="menu-item-2149" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2149"><a href="https://pythonpip.ru/tag/mongodb">MongoDB</a></li>
<li id="menu-item-2150" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2150"><a href="https://pythonpip.ru/tag/mysql">MySQL</a></li>
<li id="menu-item-2151" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2151"><a href="https://pythonpip.ru/tag/opencv">OpenCV</a></li>
<li id="menu-item-2152" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-2152"><a href="https://pythonpip.ru/tag/tkinter">Tkinter</a></li>
<li id="menu-item-3929" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-3929"><a href="https://pythonpip.ru/django">Django</a></li>
</ul></div>												</nav>
											</div><!--nav-menu-in-->
											<div class="nav-right-wrap relative">
												<div class="nav-search-wrap left relative">
													<span class="nav-search-but left"><i class="fa fa-search fa-2"></i></span>
													<div class="search-fly-wrap">
														<form method="get" id="searchform" action="https://pythonpip.ru/">
	<input type="text" name="s" id="s" value="Type search term and press enter" onfocus='if (this.value == "Type search term and press enter") { this.value = ""; }' onblur='if (this.value == "") { this.value = "Type search term and press enter"; }' />
	<input type="hidden" id="searchsubmit" value="Search" />
</form>													</div><!--search-fly-wrap-->
												</div><!--nav-search-wrap-->
																																			</div><!--nav-right-wrap-->
										</div><!--nav-menu-out-->
									</div><!--nav-logo-in-->
								</div><!--nav-logo-out-->
							</div><!--main-nav-cont-->
						</div><!--nav-in-->
					</div><!--nav-out-->
				</div><!--main-nav-wrap-->
			</div><!--head-main-wrap-->
										<div id="body-main-wrap" class="left relative" itemscope itemtype="http://schema.org/Article">
					<meta itemscope itemprop="mainEntityOfPage"  itemType="https://schema.org/WebPage" itemid="https://pythonpip.ru/examples/kak-napechatat-uzor-v-python"/>
																																			<div class="body-main-out relative">
					<div class="body-main-in">
						<div id="body-main-cont" class="left relative">
																		<div id="post-main-wrap" class="left relative">
	<div class="post-wrap-out1">
		<div class="post-wrap-in1">
			<div id="post-left-col" class="relative">
									<article id="post-area" class="post-1840 post type-post status-publish format-standard hentry category-examples">
													<header id="post-header">
																	<a class="post-cat-link" href="https://pythonpip.ru/examples"><span class="post-head-cat">Примеры</span></a>
																<h1 class="post-title entry-title left" itemprop="headline">Как напечатать узор в Python &#8211; много шаблонов с примерами</h1>
						<div class="post-info-date left relative">
														<span class="post-info-text">Опубликовано</span> <span class="post-date updated"><time class="post-date updated" itemprop="datePublished" datetime="2021-10-13">13.10.2021</time></span>
														<meta itemprop="dateModified" content="2021-10-13"/>
													</div>		
							</header><!--post-header-->
																			<div class="mvp-post-img-hide" itemprop="image" itemscope itemtype="https://schema.org/ImageObject">
																<meta itemprop="url" content="https://pythonpip.ru/wp-includes/images/media/default.png">
								<meta itemprop="width" content="48">
								<meta itemprop="height" content="64">
							</div><!--mvp-post-img-hide-->
												<div id="content-area" itemprop="articleBody" class="post-1840 post type-post status-publish format-standard hentry category-examples">
							<div class="post-cont-out">
								<div class="post-cont-in">
									<div id="content-main" class="left relative">

													<div class="mvp-post-img-hide" itemprop="image" itemscope itemtype="https://schema.org/ImageObject">
																<meta itemprop="url" content="https://pythonpip.ru/wp-includes/images/media/default.png">
								<meta itemprop="width" content="48">
								<meta itemprop="height" content="64">
							</div><!--mvp-post-img-hide-->
						
																											
																														<span id="content_pointer_id" data-content-length="4043" data-accepted-blocks="94"></span><p>В Python цикл for используется для печати различных узоров. Печать различных шаблонов &#8211; это наиболее частое задание на собеседовании по программированию. Множественные циклы for используются для печати шаблонов, где первый внешний цикл используется для печати количества строк, а внутренний цикл используется для печати количества столбцов.</p>
<p>В большинстве шаблонов используются следующие концепции:</p>
<ul class="points">
<li>Внешний цикл для вывода количества строк.</li>
<li>Внутренние циклы для печати количества столбцов.</li>
<li>Переменная для печати пробелов в соответствии с требуемым местом в Python.</li>
</ul>
<p>В этом уроке мы обсудим как напечатать узор в Python и несколько общих шаблонов.</p>
<h2>Печать пирамиды, звезды и ромбовидного узора на Python</h2>
<p>В этом разделе мы изучим общие шаблоны пирамид.</p>
<h3>Узор 1. Простая пирамида</h3>
<p>Пример &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
# This is the example of print simple pyramid pattern 
n = int(input("Enter the number of rows")) 
# outer loop to handle number of rows 
for i in range(0, n): 
    # inner loop to handle number of columns 
    # values is changing according to outer loop 
        for j in range(0, i + 1): 
            # printing stars 
            print("* ", end="")      
 
        # ending line after each row 
        print() 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">*  
* *  
* * *  
* * * *  
* * * * * 
</pre>
<p>Объяснение:</p>
<p>В приведенном выше коде мы инициализировали переменную n, чтобы ввести количество строк для шаблона. Мы ввели n = 5, диапазон внешнего цикла for будет от 0 до 4.</p>
<ul class="points">
<li>Итерация внутреннего цикла for зависит от внешнего цикла. Внутренний цикл отвечает за печать количества столбцов.</li>
<li>В первой итерации значение i равно 0, и оно увеличилось на 1, поэтому оно становится 0 + 1, теперь внутренний цикл повторяется в первый раз и выводит одну звездочку(*).</li>
<li>Во второй итерации значение i равно 1, и оно увеличилось на 1, поэтому оно становится 1 + 1, теперь внутренний цикл повторяется два раза и выводит две звезды(*).</li>
<li>Конечный аргумент предотвращает переход на другую строку. Он будет печатать звезду, пока цикл не станет действительным.</li>
<li>Последний оператор печати отвечает за завершение строки после каждого ряда.</li>
</ul>
<h3>Узор 2. Обратная пирамида под прямым углом</h3>
<p>Пример &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
# This is the example of print simple reversed right angle pyramid pattern 
rows = int(input("Enter the number of rows:")) 
k = 2 * rows - 2  # It is used for number of spaces 
for i in range(0, rows): 
    for j in range(0, k): 
        print(end=" ") 
    k = k - 2   # decrement k value after each iteration 
    for j in range(0, i + 1): 
        print("* ", end="")  # printing star 
    print("") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">      *  
     * *  
    * * *  
   * * * *  
  * * * * * 
</pre>
<h3>Шаблон 3. Печать нижней половины пирамиды</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
 
# the outer loop is executing in reversed order 
for i in range(rows + 1, 0, -1):   
    for j in range(0, i - 1): 
        print("*", end=' ') 
    print(" ") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5 
* * * * *   
* * * *   
* * *   
* *   
*   
</pre>
<h3>Шаблон 4. Печать треугольной пирамиды</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
n = int(input("Enter the number of rows: ")) 
m =(2 * n) - 2 
for i in range(0, n): 
    for j in range(0, m): 
        print(end=" ") 
    m = m - 1  # decrementing m after each loop 
    for j in range(0, i + 1): 
        # printing full Triangle pyramid using stars 
        print("* ", end=' ') 
    print(" ") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 10 
                  *    
                 *  *    
                *  *  *    
               *  *  *  *    
              *  *  *  *  *    
             *  *  *  *  *  *    
            *  *  *  *  *  *  *    
           *  *  *  *  *  *  *  *    
          *  *  *  *  *  *  *  *  *    
         *  *  *  *  *  *  *  *  *  *    
</pre>
<h3>Узор 5. Нисходящий треугольник</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
 
# It is used to print space 
k = 2 * rows - 2 
# Outer loop in reverse order 
for i in range(rows, -1, -1): 
    # Inner loop will print the number of space. 
    for j in range(k, 0, -1): 
        print(end=" ") 
    k = k + 1 
    # This inner loop will print the number o stars 
    for j in range(0, i + 1): 
        print("*", end=" ") 
    print("\r") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">                  * * * * * * * * * * *  
                   * * * * * * * * * *  
                    * * * * * * * * *  
                     * * * * * * * *  
                      * * * * * * *  
                       * * * * * *  
                        * * * * *  
                         * * * *  
                          * * *  
                           * *  
                            * 
</pre>
<h3>Шаблон 6. Ромбовидный узор</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
 
# It is used to print the space 
k = 2 * rows - 2 
# Outer loop to print number of rows 
for i in range(0, rows): 
    # Inner loop is used to print number of space 
    for j in range(0, k): 
        print(end=" ") 
    # Decrement in k after each iteration 
    k = k - 1 
    # This inner loop is used to print stars 
    for j in range(0, i + 1): 
        print("* ", end="") 
    print("") 
 
# Downward triangle Pyramid 
# It is used to print the space 
k = rows - 2 
# Output for downward triangle pyramid 
for i in range(rows, -1, -1): 
    # inner loop will print the spaces 
    for j in range(k, 0, -1): 
        print(end=" ") 
    # Increment in k after each iteration 
    k = k + 1 
    # This inner loop will print number of stars 
    for j in range(0, i + 1): 
        print("* ", end="") 
    print("") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 8 
              *  
             * *  
            * * *  
           * * * *  
          * * * * *  
         * * * * * *  
        * * * * * * *  
       * * * * * * * *  
      * * * * * * * * *  
       * * * * * * * *  
        * * * * * * *  
         * * * * * *  
          * * * * *  
           * * * *  
            * * *  
             * *  
              * 
</pre>
<h3>Шаблон 7. Печать двух пирамид в один узор</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = input("Enter the number of rows: ") 
 
# Outer loop will print the number of rows 
for i in range(0, rows): 
    # This inner loop will print the stars 
    for j in range(0, i + 1): 
        print("*", end=' ') 
    # Change line after each iteration 
    print(" ") 
# For second pattern 
for i in range(rows + 1, 0, -1): 
    for j in range(0, i - 1): 
        print("*", end=' ') 
    print(" ") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 7 
*   
* *   
* * *   
* * * *   
* * * * *   
* * * * * *   
* * * * * * *   
* * * * * * *   
* * * * * *   
* * * * *   
* * * *   
* * *   
* *   
* 
</pre>
<h3>Узор 8. Песочные часы</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
k = rows - 2 
# This is used to print the downward pyramid 
for i in range(rows, -1 , -1): 
    for j in range(k , 0 , -1): 
        print(end=" ") 
    k = k + 1 
    for j in range(0, i+1): 
        print("* " , end="") 
    print() 
 
# This is used to print the upward pyramid 
k = 2 * rows  - 2 
for i in range(0 , rows+1): 
    for j in range(0 , k): 
        print(end="") 
    k = k - 1 
    for j in range(0, i + 1): 
        print("* ", end="") 
    print() 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5 
   * * * * * *  
    * * * * *  
     * * * *  
      * * *  
       * *  
        *  
        *  
       * *  
      * * *  
     * * * *  
   * * * * *  
  * * * * * * 
</pre>
<p>Мы обсудили базовый образец пирамиды с использованием циклов for. Концепция шаблона зависит от логики и правильного использования цикла for.</p>
<h2>Числовой шаблон в Python</h2>
<p>В этом разделе мы описываем несколько программ различных типов числовых шаблонов. Давайте разберемся со следующими шаблонами один за другим.</p>
<h3>Числовой</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
# Outer loop will print number of rows 
for i in range(rows+1): 
    # Inner loop will print the value of i after each iteration 
    for j in range(i): 
        print(i, end=" ")  # print number 
    # line after each row to display pattern correctly 
    print(" ") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5 
1   
2 2   
3 3 3   
4 4 4 4   
5 5 5 5 5   
</pre>
<p>Объяснение &#8211;</p>
<p>В приведенном выше коде мы напечатали числа в соответствии со значением строк. В первой строке печатается одно число. Затем два числа печатаются во втором ряду, а следующие три числа печатаются в третьем ряду и так далее. в</p>
<h3>Полупирамида с цифрой</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
 
# This will print the rows 
for i in range(1, rows+1): 
    # This will print number of column 
    for j in range(1, i + 1): 
        print(j, end=' ') 
    print("") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5 
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5 
</pre>
<p>В приведенном выше коде мы напечатали значение столбца j во внутреннем цикле for.</p>
<h3>Узор перевернутой пирамиды</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: 5")) 
k = 0 
# Reversed loop for downward inverted pattern 
for i in range(rows, 0, -1): 
    # Increment in k after each iteration 
    k += 1 
    for j in range(1, i + 1): 
        print(k, end=' ') 
    print() 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5 
1 1 1 1 1  
2 2 2 2  
3 3 3  
4 4  
5 
</pre>
<p>Объяснение:</p>
<p>В приведенном выше коде мы использовали обратный цикл для печати перевернутой вниз пирамиды, где число уменьшалось после каждой итерации.</p>
<h3>Перевернутая пирамида с тем же номером</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
# rows value assign to n variable 
n = rows 
# Download reversed loop 
for i in range(rows, 0, -1): 
    for j in range(0, i): 
        # this will print the same number 
        print(n, end=' ') 
    print() 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 6 
6 6 6 6 6 6  
6 6 6 6 6  
6 6 6 6  
6 6 6  
6 6  
6 
</pre>
<h3>Порядок убывания числа</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
# Downward loop for inverse loop 
for i in range(rows, 0, -1): 
    n = i   # assign value to n of i after each iteration 
    for j in range(0, i): 
        # print reduced value in each new line 
        print(n, end=' ') 
    print("\r") 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 6 
6 6 6 6 6 6  
5 5 5 5 5  
4 4 4 4  
3 3 3  
2 2  
1 
</pre>
<h3>Печать чисел от 1 до 10  в шаблоне</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
current_Number = 1 
stop = 2 
rows = 3  # Number of rows to print numbers 
 
for i in range(rows): 
    for j in range(1, stop): 
        print(current_Number, end=' ') 
        current_Number += 1 
    print("") 
    stop += 2 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">1  
2 3 4  
5 6 7 8 9 
</pre>
<h3>Обратный шаблон от 10 до 1</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python"> 
rows = int(input("Enter the number of rows: ")) 
for i in range(0, rows + 1): 
    # inner loop for decrement in i values 
    for j in range(rows - i, 0, -1): 
        print(j, end=' ') 
    print() 
</pre>
<p>Выход:</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 6 
6 5 4 3 2 1  
5 4 3 2 1  
4 3 2 1  
3 2 1  
2 1  
1 
</pre>
<h3>Печать нечетных чисел</h3>
<p>Код &#8211;</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">rows = int(input("Enter the number of rows: "))
i = 1
# outer file loop to print number of rows
while i
</pre>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9</pre>
<h3>Квадратный узор с использованием номера</h3>
<pre class="EnlighterJSRAW" data-enlighter-language="python">rows = int(input("Enter the number of rows: "))  
for i in range(1, rows + 1):  
    for j in range(1, rows + 1):  
        # Check condition if value of j is smaller or equal than  
        # the j then print i otherwise print j  
        if j &lt;= i:  
            print(i, end=' ')  
        else:  
            print(j, end=' ')  
    print()</pre>
<p>Вывод</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 5
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5</pre>
<h3>Умножения в столбце</h3>
<pre class="EnlighterJSRAW" data-enlighter-language="python">rows = int(input("Enter the number of rows: "))  
for i in range(1, rows):  
    for j in range(1, i + 1):  
        # It prints multiplication or row and column  
        print(i * j, end='  ')  
    print()</pre>
<p>Вывод</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Enter the number of rows: 8
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49</pre>
<p>В предыдущем разделе мы обсудили все основные шаблоны чисел.</p>
<p>Как мы знаем, каждый алфавит имеет собственное значение ASCII, поэтому определите символ и выведите его на экран. Давайте разберемся в этих закономерностях на следующих примерах.</p>
<h3>Прямоугольный узор с иероглифами</h3>
<pre class="EnlighterJSRAW" data-enlighter-language="python">print("The character pattern ")  
asciiValue = 65     #ASCII value of A  
for i in range(0, 5):  
    for j in range(0, i + 1):  
        # It will convert the ASCII value to the character  
        alphabate = chr(asciiValue)  
        print(alphabate, end=' ')  
        asciiValue += 1  
    print()</pre>
<p>Вывод</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">The character pattern 
A 
B C 
D E F 
G H I J 
K L M N O</pre>
<p>В приведенном выше коде мы присвоили целочисленное значение 65 переменной asciiValue, которая является значением ASCII A. Мы определили цикл for для печати пяти строк. В теле внутреннего цикла мы преобразовали значение ASCII в символ с помощью функции char(). Она будет печатать буквы, увеличивая asciiValue после каждой итерации.</p>
<h3>Прямоугольный узор с одинаковым символом</h3>
<pre class="EnlighterJSRAW" data-enlighter-language="python">print("The character pattern ")  
asciiValue = int(input("Enter the ASCII value to print pattern: "))  
# User - define value  
if (asciiValue &gt;= 65 or asciiValue &lt;=122):  
    for i in range(0, 5):  
        for j in range(0, i + 1):  
            # It will convert the ASCII value to the character  
            alphabate = chr(asciiValue)  
            print(alphabate, end=' ')  
        print()  
else:  
    print("Enter the valid character value")</pre>
<p>Вывод</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">The character pattern 
Enter the ASCII value to print pattern: 75
K 
K K 
K K K 
K K K K 
K K K K K</pre>
<h3>Вывод слова по буквам</h3>
<pre class="EnlighterJSRAW" data-enlighter-language="generic">str1 = "pythonpip"  
x = ""  
for i in str1:  
    x += i  
    print(x)</pre>
<p>Вывод</p>
<pre class="EnlighterJSRAW" data-enlighter-language="generic">p
pi
pit
pith
pitho
python
pythonp
pythonpi
pythonpip</pre>
<h3>Равносторонний треугольник с символами</h3>
<pre class="EnlighterJSRAW" data-enlighter-language="python">print("Print equilateral triangle Pyramid with characters ")  
s = 5  
asciiValue = 65  
m = (2 * s) - 2  
for i in range(0, s):  
    for j in range(0, m):  
        print(end=" ")  
    # Decreased the value of after each iteration  
    m = m - 1  
    for j in range(0, i + 1):  
        alphabate = chr(asciiValue)  
        print(alphabate, end=' ')  
        # Increase the ASCII number after each iteration  
        asciiValue += 1  
    print()</pre>
<p>Вывод</p>
<pre class="EnlighterJSRAW" data-enlighter-language="python">Print equilateral triangle Pyramid with characters 
        A 
       B C 
      D E F 
     G H I J 
    K L M N O</pre>
<p>Эти шаблоны обычно задают во время собеседования, и это также полезно для понимания концепции цикла for в Python. Как только мы получим логику программы, мы можем распечатать любой шаблон.</p>
<script>
window.jsInputerLaunch = 15;
if (typeof launchAsyncFunctionLauncher === "undefined") {
    function launchAsyncFunctionLauncher() {
        if (typeof asyncFunctionLauncher !== "undefined" && typeof asyncFunctionLauncher === "function") {
            asyncFunctionLauncher();
        } else {
            setTimeout(function () {
                launchAsyncFunctionLauncher();
            }, 100)
        }
    }
}
launchAsyncFunctionLauncher();
</script><script>
var cachedBlocksArray = [];
</script>																														<div class="mvp-org-wrap" itemprop="publisher" itemscope itemtype="https://schema.org/Organization">
											<div class="mvp-org-logo" itemprop="logo" itemscope itemtype="https://schema.org/ImageObject">
																									<img src="https://pythonpip.ru/wp-content/uploads/logotip.png"/>
													<meta itemprop="url" content="https://pythonpip.ru/wp-content/uploads/logotip.png">
																							</div><!--mvp-org-logo-->
											<meta itemprop="name" content="Python самоучитель для начинающих">
										</div><!--mvp-org-wrap-->
										<div class="posts-nav-link">
																						
										</div><!--posts-nav-link-->
										
										<!--noindex-->																			<div id="post-info-wrap" class="left relative">
										<div class="post-info-out">
											<div class="post-info-img left relative">
												<img src="//pythonpip.ru/wp-content/uploads/mihail.jpg" >
											</div><!--post-info-img-->
											<div class="post-info-in">
												<div class="post-info-right left relative">
													<div class="post-info-name left relative" itemprop="author" itemscope itemtype="https://schema.org/Person">
														<span class="post-info-text"></span> <span class="author-name vcard fn author" itemprop="name"><a href="https://pythonpip.ru/author/adminpip" title="Записи Михаил Русаков" rel="author">Михаил Русаков</a></span>  														
													</div><!--post-info-name-->
													<div class="post-info-date left relative">
														Изучаю Python вместе с вами, читаю, собираю и записываю информацию опытных программистов.													</div><!--post-info-date-->
												</div><!--post-info-right-->
											</div><!--post-info-in-->
										</div><!--post-info-out-->
									</div><!--post-info-wrap-->
										<!--/noindex-->
																			<div class="post-tags">
												<span class="post-tags-header">Еще для изучения:</span>
												<!-- relpost-thumb-wrapper --><div class="relpost-thumb-wrapper"><!-- filter-class --><div class="relpost-thumb-container"><div style="clear: both"></div><div style="clear: both"></div><!-- relpost-block-container --><div class="relpost-block-container"><a class="relpost-block-single" href="https://pythonpip.ru/examples/nastroyka-sredy-mysql-python-i-ustanovka-mysql-connector"><div class="relpost-custom-block-single" style="width: 150px; height: 105px;"><div class="relpost-block-single-text"  style="font-family: 'Montserrat', sans-serif;  font-size: 18px;  color: #333333;">Настройка среды MySQL Python и установка mysql.connector</div></div></a><a class="relpost-block-single" href="https://pythonpip.ru/examples/vstavka-uzla-v-nachalo-i-konets-krugovogo-svyazannogo-spiska-v-python"><div class="relpost-custom-block-single" style="width: 150px; height: 105px;"><div class="relpost-block-single-text"  style="font-family: 'Montserrat', sans-serif;  font-size: 18px;  color: #333333;">Вставка узла в начало и конец кругового связанного списка в Python</div></div></a><a class="relpost-block-single" href="https://pythonpip.ru/examples/stek-python"><div class="relpost-custom-block-single" style="width: 150px; height: 105px;"><div class="relpost-block-single-text"  style="font-family: 'Montserrat', sans-serif;  font-size: 18px;  color: #333333;">Стек в Python - основы и примеры</div></div></a><a class="relpost-block-single" href="https://pythonpip.ru/examples/sozdanie-kalkulyatora-imt-s-pomoschyu-python"><div class="relpost-custom-block-single" style="width: 150px; height: 105px;"><div class="relpost-block-single-text"  style="font-family: 'Montserrat', sans-serif;  font-size: 18px;  color: #333333;">Создание калькулятора ИМТ с помощью Python</div></div></a></div><!-- close relpost-block-container --><div style="clear: both"></div></div><!-- close filter class --></div><!-- close relpost-thumb-wrapper -->											</div><!--post-tags-->
										
																				
																					<div class="social-sharing-bot">
											<script src="//yastatic.net/es5-shims/0.0.2/es5-shims.min.js" async="async"></script>
<script src="//cdn.jsdelivr.net/npm/yandex-share2/share.js" async="async"></script>
<div class="ya-share2 ya-share2_horizontal" data-services="vkontakte,telegram,viber"></div>
											</div><!--social-sharing-bot-->
										
																																								
																																													<div id="comments-button" class="left relative comment-click-1840 com-but-1840">
													<span class="comment-but-text">Оставить комментарий</span>
												</div><!--comments-button-->
												<div id="comments" class="com-click-id-1840 com-click-main">
				
	
<!--noindex-->	<div id="respond" class="comment-respond">
		<span id="reply-title" class="sidebar-top group">Добавить комментарий</span><form action="https://pythonpip.ru/wp-comments-post.php" method="post" id="commentform" class="comment-form"><p class="comment-notes"><span id="email-notes">Ваш адрес email не будет опубликован.</span> <span class="required-field-message">Обязательные поля помечены <span class="required">*</span></span></p><p class="comment-form-comment"><label for="comment">Комментарий <span class="required">*</span></label> <textarea id="comment" name="comment" cols="45" rows="8" maxlength="65525" required="required"></textarea></p><p class="comment-form-author"><label for="author">Имя <span class="required">*</span></label> <input id="author" name="author" type="text" value="" size="30" maxlength="245" autocomplete="name" required="required" /></p>
<p class="comment-form-email"><label for="email">Email <span class="required">*</span></label> <input id="email" name="email" type="text" value="" size="30" maxlength="100" aria-describedby="email-notes" autocomplete="email" required="required" /></p>
<p class="comment-form-cookies-consent"><input id="wp-comment-cookies-consent" name="wp-comment-cookies-consent" type="checkbox" value="yes" /> <label for="wp-comment-cookies-consent">Сохранить моё имя, email и адрес сайта в этом браузере для последующих моих комментариев.</label></p>
<p class="form-submit"><input name="submit" type="submit" id="submit" class="submit" value="Отправить комментарий" /> <input type='hidden' name='comment_post_ID' value='1840' id='comment_post_ID' />
<input type='hidden' name='comment_parent' id='comment_parent' value='0' />
</p></form>	</div><!-- #respond -->
	<!--/noindex-->

</div><!--comments-->										
																														</div><!--content-main-->
								</div><!--post-cont-in-->
															</div><!--post-cont-out-->
						</div><!--content-area-->
					</article>
										
						
	<nav class="navigation post-navigation" aria-label="Записи">
		<h2 class="screen-reader-text">Навигация по записям</h2>
		<div class="nav-links"><div class="nav-previous"><a href="https://pythonpip.ru/examples/kak-nayti-vtoroe-po-velichine-chislo-v-spiske-python" rel="prev">4 способа как найти второе по величине число в списке Python</a></div><div class="nav-next"><a href="https://pythonpip.ru/examples/silnoe-chislo-strong-number-v-python-chto-takoe-i-kak-opredelit" rel="next">Сильное число(Strong Number) в Python &#8211; что такое и как определить</a></div></div>
	</nav>																			</div><!--post-left-col-->
			</div><!--post-wrap-in1-->
							<div id="post-right-col" class="relative">
																		<div id="sidebar-wrap" class="left relative theiaStickySidebar">
						<div id="mvp_pop_widget-2" class="side-widget mvp_pop_widget"><div class="post-header"><span class="post-tags">Популярные</span></div>			<div class="blog-widget-wrap left relative">
				<ul class="blog-widget-list left relative">
											<li>
							<a href="https://pythonpip.ru/osnovy/primer-prostoy-programmy-python" rel="bookmark">
														<div class="blog-widget-text left relative">
								
								<div>Пример простой программы на Python &#8211; пишем с нуля</div>
								<p>В этом разделе мы обсудим основной синтаксис и разберем пример Python &#8211; запустим простую...</p>
							</div><!--blog-widget-text-->
							</a>
						</li>
											<li>
							<a href="https://pythonpip.ru/examples/kak-sozdat-dataframes-pandas-v-python-7-metodov" rel="bookmark">
														<div class="blog-widget-text left relative">
								
								<div>Как создать DataFrames Pandas в Python &#8211; 7 методов</div>
								<p>Фрейм данных &#8211; это двухмерный набор данных, структура, в которой данные хранятся в табличной...</p>
							</div><!--blog-widget-text-->
							</a>
						</li>
											<li>
							<a href="https://pythonpip.ru/examples/funktsiya-strip-v-python" rel="bookmark">
														<div class="blog-widget-text left relative">
								
								<div>Функция strip() в Python</div>
								<p>Функция strip() &#8211; это предопределенная библиотечная функция Python. Она используется для возврата копии исходной...</p>
							</div><!--blog-widget-text-->
							</a>
						</li>
											<li>
							<a href="https://pythonpip.ru/examples/matritsa-python" rel="bookmark">
														<div class="blog-widget-text left relative">
								
								<div>Матрица в Python &#8211; основы работы</div>
								<p>В этой статье мы познакомим вас с матрицей Python. Каждую операцию матрицы мы будем...</p>
							</div><!--blog-widget-text-->
							</a>
						</li>
									</ul>
			</div><!--blog-widget-wrap-->
		</div><div id="custom_html-2" class="widget_text side-widget widget_custom_html"><div class="textwidget custom-html-widget"><div id="adfox_163283040868919067"></div>
<script>
    window.yaContextCb.push(()=>{
        Ya.adfoxCode.createAdaptive({
            ownerId: 260971,
        containerId: 'adfox_163283040868919067',
            params: {
                p1: 'cqutb',
            p2: 'gxmq'
            }
        }, ['desktop', 'tablet'], {
            tabletWidth: 830,
            phoneWidth: 480,
            isAutoReloads: false
        })
    })
</script>
<script>
setInterval(function(){            
window.Ya.adfoxCode.reload('adfox_163283040868919067')
}, 30000);
</script></div></div>			</div><!--sidebar-wrap-->															</div><!--post-right-col-->
					</div><!--post-wrap-out1-->
</div><!--post-main-wrap-->
											</div><!--body-main-cont-->
				</div><!--body-main-in-->
			</div><!--body-main-out-->
			<footer id="foot-wrap" class="left relative">
				<div id="foot-top-wrap" class="left relative">
					<div class="body-main-out relative">
						<div class="body-main-in">
							<div id="foot-widget-wrap" class="left relative">
																							</div><!--foot-widget-wrap-->
						</div><!--body-main-in-->
					</div><!--body-main-out-->
				</div><!--foot-top-->
				<div id="foot-bot-wrap" class="left relative">
					<div class="body-main-out relative">
						<div class="body-main-in">
							<div id="foot-bot" class="left relative">
								<div class="foot-menu relative">
									<div class="menu-menyu-niz-container"><ul id="menu-menyu-niz" class="menu"><li id="menu-item-19" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-privacy-policy menu-item-19"><a href="https://pythonpip.ru/privacy-policy">Политика конфиденциальности</a></li>
<li id="menu-item-20" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-20"><a href="https://pythonpip.ru/kontakty">О сайте  Контакты</a></li>
</ul></div>								</div><!--foot-menu-->
								<div class="foot-copy relative">
									<p>Copyright © 2021</p>
								</div><!--foot-copy-->
							</div><!--foot-bot-->
						</div><!--body-main-in-->
					</div><!--body-main-out-->
				</div><!--foot-bot-->
			</footer>
		</div><!--body-main-wrap-->
	</div><!--site-wrap-->
</div><!--site-->
<div class="fly-to-top back-to-top">
	<i class="fa fa-angle-up fa-3"></i>
	<span class="to-top-text">Наверх</span>
</div><!--fly-to-top-->
<div class="fly-fade">
</div><!--fly-fade-->
<script>var pseudo_links = document.querySelectorAll(".pseudo-clearfy-link");for (var i=0;i<pseudo_links.length;i++ ) { pseudo_links[i].addEventListener("click", function(e){   window.open( e.target.getAttribute("data-uri") ); }); }</script><script>document.addEventListener("copy", (event) => {var pagelink = "\nИсточник: https://pythonpip.ru/examples/kak-napechatat-uzor-v-python";event.clipboardData.setData("text", document.getSelection() + pagelink);event.preventDefault();});</script>    <script type="text/javascript">function GoTo(link){window.open(link.replace("_","https://"));}</script>
    
<script type="text/javascript">
jQuery(document).ready(function($) {

	// Back to Top Button
    	var duration = 500;
    	$('.back-to-top').click(function(event) {
          event.preventDefault();
          $('html, body').animate({scrollTop: 0}, duration);
          return false;
	});

	// Main Menu Dropdown Toggle
	$('.menu-item-has-children a').click(function(event){
	  event.stopPropagation();
	  location.href = this.href;
  	});

	$('.menu-item-has-children').click(function(){
    	  $(this).addClass('toggled');
    	  if($('.menu-item-has-children').hasClass('toggled'))
    	  {
    	  $(this).children('ul').toggle();
	  $('.fly-nav-menu').getNiceScroll().resize();
	  }
	  $(this).toggleClass('tog-minus');
    	  return false;
  	});

	// Main Menu Scroll
	$(window).load(function(){
	  $('.fly-nav-menu').niceScroll({cursorcolor:"#888",cursorwidth: 7,cursorborder: 0,zindex:999999});
	});

	  	$(".comment-click-1840").on("click", function(){
  	  $(".com-click-id-1840").show();
	  $(".disqus-thread-1840").show();
  	  $(".com-but-1840").hide();
  	});
	
	// Infinite Scroll
	$('.infinite-content').infinitescroll({
	  navSelector: ".nav-links",
	  nextSelector: ".nav-links a:first",
	  itemSelector: ".infinite-post",
	  loading: {
		msgText: "Загружаю...",
		finishedMsg: "Извините, больше нет"
	  },
	  errorCallback: function(){ $(".inf-more-but").css("display", "none") }
	});
	$(window).unbind('.infscr');
	$(".inf-more-but").click(function(){
   		$('.infinite-content').infinitescroll('retrieve');
        	return false;
	});
	$(window).load(function(){
		if ($('.nav-links a').length) {
			$('.inf-more-but').css('display','inline-block');
		} else {
			$('.inf-more-but').css('display','none');
		}
	});

$(window).load(function() {
  // The slider being synced must be initialized first
  $('.post-gallery-bot').flexslider({
    animation: "slide",
    controlNav: false,
    animationLoop: true,
    slideshow: false,
    itemWidth: 80,
    itemMargin: 10,
    asNavFor: '.post-gallery-top'
  });

  $('.post-gallery-top').flexslider({
    animation: "fade",
    controlNav: false,
    animationLoop: true,
    slideshow: false,
    	  prevText: "&lt;",
          nextText: "&gt;",
    sync: ".post-gallery-bot"
  });
});

});

</script>

      <script>
            jQuery(document).ready(function ($) {
                $('article table').wrap('<div class="table-resp"></div>');
            });
      </script>
      <style>
         @media screen and (max-width: 1035px) {
            .table-resp {
               width: 100%;
               overflow: auto;
               margin: 0 0 1em;
            }
         }
      </style>
      <script type='text/javascript' src='https://pythonpip.ru/wp-includes/js/comment-reply.min.js' id='comment-reply-js'></script>
<script type='text/javascript' src='https://pythonpip.ru/wp-content/themes/flex-mag/js/scripts.js' id='mvp-flexmag-js'></script>
<script type='text/javascript' src='https://pythonpip.ru/wp-content/themes/flex-mag/js/jquery.infinitescroll.min.js' id='mvp-infinitescroll-js'></script>
<script type='text/javascript' src='https://pythonpip.ru/wp-content/themes/flex-mag/js/autoloadpost.js' id='mvp-autoloadpost-js'></script>
<script type='text/javascript' src='https://pythonpip.ru/wp-content/themes/flex-mag/js/retina.js' id='retina-js'></script>
<script type='text/javascript' id='q2w3_fixed_widget-js-extra'>
/* <![CDATA[ */
var q2w3_sidebar_options = [{"sidebar":"sidebar-widget-post","use_sticky_position":false,"margin_top":0,"margin_bottom":0,"stop_elements_selectors":"","screen_max_width":0,"screen_max_height":0,"widgets":["#custom_html-2"]}];
/* ]]> */
</script>
<script type='text/javascript' src='https://pythonpip.ru/wp-content/plugins/q2w3-fixed-widget/js/frontend.min.js' id='q2w3_fixed_widget-js'></script>
<script type='text/javascript' src='https://pythonpip.ru/wp-content/plugins/enlighter/cache/enlighterjs.min.js' id='enlighterjs-js'></script>
<script type='text/javascript' id='enlighterjs-js-after'>
!function(e,n){if("undefined"!=typeof EnlighterJS){var o={"selectors":{"block":"pre.EnlighterJSRAW","inline":"code.EnlighterJSRAW"},"options":{"indent":4,"ampersandCleanup":true,"linehover":true,"rawcodeDbclick":false,"textOverflow":"break","linenumbers":true,"theme":"atomic","language":"generic","retainCssClasses":false,"collapse":false,"toolbarOuter":"","toolbarTop":"{BTN_RAW}{BTN_COPY}{BTN_WINDOW}{BTN_WEBSITE}","toolbarBottom":""}};(e.EnlighterJSINIT=function(){EnlighterJS.init(o.selectors.block,o.selectors.inline,o.options)})()}else{(n&&(n.error||n.log)||function(){})("Error: EnlighterJS resources not loaded yet!")}}(window,console);
!function(e){"undefined"!=typeof jQuery&&jQuery(document).on("ajaxComplete",function(){"undefined"!=typeof EnlighterJSINIT&&e.setTimeout(function(){EnlighterJSINIT.apply(e)},180)})}(window);
</script>
<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(70769212, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/70769212" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
<!-- Yandex.RTB R-A-1301849-3 -->
<script>window.yaContextCb.push(()=>{
  Ya.Context.AdvManager.render({
    type: 'floorAd',
    blockId: 'R-A-1301849-3'
  })
})</script>

</body>
</html>

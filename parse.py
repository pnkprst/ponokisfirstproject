def media(i_text: str, spliter="||") -> str:
    elems = i_text.replace("&amp\\;", "&").split(spliter)
    l_text = ""
    if elems[0][0] == ":" and elems[0][-1] == ":":
        return "<a href=\"" + elems[0][1:len(elems[0])-1] + "\" width=\"120\">"
    elif len(elems) == 1:
        return "<a href=\"" + elems[0] + "\">" + elems[0] + "</a>"
    elif len(elems) == 2:
        return "<a href=\"" + elems[0] + "\" title=\"" + elems[1] + "\">" + elems[1] + "</a>"
    elif len(elems) == 3:
        if elems[2] in ("l", "link"):
            return "<a href=\"" + elems[0] + "\" title=\"" + elems[1] + "\">" + elems[1] + "</a>"
        elif elems[2] in ("img", "i", "imag", "image"):
            return "<a href=\"" + elems[0] + "\"><img src=\"" \
                   + elems[0] + "\" alt=\"" + elems[1] + "\" title=\"" + elems[1] + "\" width=\"540\" />" \
                   "</a>"
        elif elems[2] in ("a", "aud", "audio"):
            return "<figure><figcaption>" + hyper(elems[1], '|') + "</figcaption>" \
                   "<audio controls src=\"" + elems[0] + "\">" + "음악재생: " + hyper(elems[1], '|') + "</audio>" \
                   "<figure>"
        else:
            return "<a href=\"" + elems[0] + "\" title=\"" + elems[1] + "\">" + elems[2] + ": " + elems[1] + "</a>"
    else:
        if elems[2] in ("c", "cd", "code"):
            return hyper(elems[0], '|') + "<pre class=\"" + elems[1] + "\"><code>" + elems[3] + "</code></pre>"
        elif elems[2] in ("b", "bq", "block", "blockquote"):
            return hyper(elems[0], '|') + "<blockquote>" + hyper(elems[3], '|') + "</blockquote>"
        elif elems[2] in ("d", "dt", "details"):
            return "<details><summary>" + hyper(elems[0], '|') + "</summary>" + hyper(elems[3], '|') + "</details>"
        elif elems[2] in ("u", "un", "uo", "unorder"):
            for i in elems[3:]:
                l_text += "<li>" + hyper(i, '|') + "</li>"
            return hyper(elems[0], '|') + "<ul>" + l_text + "</ul>"
        elif elems[2] in ("o", "or", "order"):
            for i in elems[3:]:
                l_text += "<li>" + hyper(i, '|') + "</li>"
            return hyper(elems[0], '|') + "<ol>" + l_text + "</ol>"
        elif elems[2] in ("t", "tbl", "table"):
            return "<table><caption>" + hyper(elems[0], '|') + "</caption>" + table(elems[3]) + "</table>"

        else:
            return "<a href=\"" + elems[0] + "\" title=\"" + elems[1] + "\">" + elems[2] + ": " + elems[1] + "</a>"


def hyper(i_text: str, spliter="||") -> str:
    tags = {
        '*': "strong",
        '/': "em",
        '_': "ins",
        '-': "del",
        '~': "span style=\"color:gray\"",
        '%': "span style=\"color:red\"",
        '`': "code"
    }
    escape = {
        '<': "&lt\\;",
        '>': "&rt\\;",
        '&': "&amp\\;"
    }
    rollback = False
    sup = False
    sub = False
    tagged = []
    apptag = []
    t_text = ""
    o_text = ""
    mover = False
    sender = ""
    for i in i_text:
        if i in escape.keys():
            t_text += escape[i]
        else:
            t_text += i
    for i in t_text:
        if mover:
            if i == ']':
                mover = False
                o_text += media(sender, spliter)
                sender = ""
            else:
                sender += i
        elif rollback:
            o_text += "<br>" if i == '\n' else i
            rollback = False
        elif i == "=":
            o_text += "<hr />"
        elif i == "@":
            o_text += "&#09;"
        elif i == '[':
            mover = True
        elif sup:
            o_text += "<sup>" + i + "</sup>"
            sup = False
        elif sub:
            o_text += "<sub>" + i + "</sub>"
            sub = False
        elif i == '\n':
            continue
        elif i == '\\':
            rollback = True
        elif i == '^':
            sup = True
        elif i == ';':
            sub = True
        elif i in tags.keys():
            if tags[i] not in tagged:
                o_text += "<" + tags[i] + ">"
                tagged.append(tags[i])
            elif tags[i] == tagged[-1]:
                o_text += "</" + tags[i].split()[0] + ">"
                tagged.pop()
            else:
                while True:
                    apptag.append(tagged[-1])
                    o_text += "</" + apptag[-1].split()[0] + ">"
                    if tags[i] == tagged[-1]:
                        tagged.pop()
                        apptag.pop()
                        break
                    tagged.pop()
                for j in apptag:
                    o_text += "<" + j + ">"
                    tagged.append(j)
                apptag.clear()
        else:
            o_text += i
    for i in tagged[::-1]:
        o_text += "</" + i.split()[0] + ">"
    return o_text


def table(i_str: str) -> str:
    return "<tr><th>표기능 제공예정<th></tr><tr><td>" + i_str + "</td></tr>"


if __name__ == "__main__":
    print(hyper("*Strong*"))

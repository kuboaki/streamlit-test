import streamlit as st # type: ignore

st.title("今日の運勢占い")
st.header("あなたの運勢を占います")

name = st.text_input("あなたの名前を教えてください",
                        placeholder="例: 山田太郎",
                        help = "2から20文字で入力してください。ニックネームでもOKです",
                        max_chars=20)
if name:
    if name.lower() in ["先生", "teacher", "sensei"]:
        st.balloons()
        st.subheader(f"{name}さんの今日の総合運")
        st.success("特大吉！いつもありがとうございます！")
        st.info("きょうは特別な一日になるでしょう。")
    elif "python" in name.lower():
        st.subheader(f"{name}さんの今日の総合運")
        st.success("大吉！Pythonのプログラミングがうまくいく日です。")
        st.info("きょうはコードがスラスラ書ける日です！！")        
    else:
        st.subheader(f"{name}さんの今日の総合運")
        st.success("大吉です！素晴らしい一日になるでしょう。")

        st.divider()
        st.info(f"**{name}さんへのアドバイス:**")
        st.write(f"きょうの{name}さんは、特に午後から運気が上昇します。")
        st.write(f"{name}さんにとって大切な人との縁が深まる日です。")
        st.write(f"ラッキカラー：青（{name}さんの運気をサポート）")
else:
    st.info("名前を入力して、個人占いを始めましょう。")


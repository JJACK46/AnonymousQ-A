import { useState } from "react";
import "../assets/App.css";
import { MdFileCopy, MdCheck, MdOutlineContentPaste } from "react-icons/md";

function App() {
  const [key, setKey] = useState<string | null>(null);
  const [room, setRoom] = useState<string | null>(null);
  const [isCopied, setIsCopied] = useState(false);

  function generateRandomKey() {
    const randomNum = Math.floor(Math.random() * 900000) + 100000;
    setKey(String(randomNum));
  }

  const copyToClipboard = () => {
    navigator.clipboard
      .writeText(key!)
      .then(() => {
        setIsCopied(true);
      })
      .catch((error) => {
        console.error("Failed to copy: ", error);
      });
  };
  const handlePaste = async () => {
    navigator.clipboard
      .readText()
      .then((text) => {
        setRoom(text);
      })
      .catch((err) => {
        console.error("Failed to read clipboard:", err);
      });
  };

  return (
    <>
      <img
        draggable={false}
        className="w-32 mx-auto mb-5"
        src="/safe-svgrepo-com.svg"
        alt="logo"
      />
      <section className="flex flex-col gap-10">
        <h1 className="text-5xl ">Anonymous Q&A</h1>
        <div className="flex flex-col self-center gap-5">
          <div className="flex rounded-md place-content-center items-center bg-black">
            <input
              type="text"
              value={key!}
              className={`flex text-center h-16 bg-transparent focus:outline-none`}
            />
            {isCopied && <MdCheck />}
            {key && !isCopied && <MdFileCopy onClick={copyToClipboard} />}
          </div>
          <button
            onClick={generateRandomKey}
            name="btnGenerate"
            className="text-xl outline rounded-md outline-2 p-2 w-64"
          >
            Generate Room Code
          </button>
          <div className="flex rounded-md place-content-center items-center bg-black">
            <input
              type="text"
              value={room ?? undefined}
              className={`flex text-center h-16 bg-transparent focus:outline-none`}
            />
            <MdOutlineContentPaste onClick={handlePaste} />
          </div>
          <button
            name="btnJoin"
            className="text-xl outline rounded-md outline-2 p-2 w-64"
          >
            Join Room
          </button>
          <div className="flex py-2 rounded-md place-content-center items-center bg-black">
            <textarea
              className={`flex h-32 bg-transparent focus:outline-none`}
            />
          </div>
          <button
            name="btnQ"
            className="text-xl outline rounded-md outline-2 p-2 w-64"
          >
            Send
          </button>
        </div>
      </section>
    </>
  );
}

export default App;

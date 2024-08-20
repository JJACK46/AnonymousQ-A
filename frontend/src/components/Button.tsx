export default function Button({
  text,
  callback,
}: {
  text: string;
  callback: () => void;
}) {
  return (
    <button
      onClick={callback}
      name="btnGenerate"
      className="text-xl outline rounded-md outline-2 p-2 w-64"
    >
      {text}
    </button>
  );
}

// export default Button;

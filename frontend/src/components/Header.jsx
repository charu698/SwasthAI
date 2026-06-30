function Header() {
  return (
    <header className="bg-white shadow-md">

      <div className="max-w-7xl mx-auto px-8 py-5 flex justify-between items-center">

        <h2 className="text-3xl font-bold text-blue-600">
          🩺 SwasthAI
        </h2>

        <nav className="flex gap-8 text-slate-700">

          <a href="#">Home</a>

          <a href="#">Features</a>

          <a href="#">About</a>

          <a href="#">Contact</a>

        </nav>

      </div>

    </header>
  );
}

export default Header;
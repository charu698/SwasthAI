import Header from "../components/Header";
import Hero from "../components/Hero";
import UploadBox from "../components/UploadBox";

function Home() {
  return (
    <div className="min-h-screen bg-slate-50">

      <Header />

      <Hero />

      <div className="flex justify-center pb-20">

        <UploadBox />

      </div>

    </div>
  );
}

export default Home;
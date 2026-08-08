export default function Admin() {
  return (
    <main className="min-h-screen bg-black text-white p-10">
      <h1 className="text-4xl font-serif mb-6">Admin Panel</h1>
      <form className="space-y-4 max-w-md" onSubmit={e => { e.preventDefault(); alert('Image uploaded (simulated)'); }}>
        <input type="file" accept="image/*" className="block w-full p-3 border border-white/20 rounded bg-[#1E1E1E]" />
        <button type="submit" className="px-6 py-3 bg-[#C8A96A] text-black font-bold rounded">Upload Image</button>
      </form>
    </main>
  );
}

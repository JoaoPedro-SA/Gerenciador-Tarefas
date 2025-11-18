import Link from "next/link";
import {
  CheckCircle2,
  Calendar,
  Users,
  BarChart3,
  Clock,
  Zap,
} from "lucide-react";
import "../global.css";

export default async function RootLayout() {
  const features = [
    {
      icon: CheckCircle2,
      title: "Gestão Completa",
      description:
        "Crie, edite e organize todas as suas tarefas em um único lugar",
    },
    {
      icon: Calendar,
      title: "Controle de Prazos",
      description: "Nunca perca um deadline com alertas visuais de prazo",
    },
    {
      icon: Users,
      title: "Múltiplos Usuários",
      description: "Gerencie tarefas de toda sua equipe de forma centralizada",
    },
    {
      icon: BarChart3,
      title: "Filtros Inteligentes",
      description: "Encontre rapidamente o que precisa com busca e filtros",
    },
    {
      icon: Clock,
      title: "Status em Tempo Real",
      description: "Acompanhe o status de cada tarefa instantaneamente",
    },
    {
      icon: Zap,
      title: "Interface Rápida",
      description: "Design otimizado para máxima produtividade",
    },
  ];

  return (
    <html>
      <body>
        <div className="min-h-screen bg-gray-50">
          {/* Hero Section */}
          <section className="relative overflow-hidden bg-gradient-to-br from-blue-600 via-blue-500 to-blue-400 text-white">
            <div className="container mx-auto px-4 py-20 md:py-32 relative z-10">
              <div className="max-w-3xl mx-auto text-center">
                <h1 className="text-4xl md:text-6xl font-bold mb-6">
                  Organize suas Tarefas com Eficiência
                </h1>
                <p className="text-lg md:text-xl mb-8 opacity-95">
                  Sistema completo de agendamento e gerenciamento de tarefas
                  para você e sua equipe
                </p>
                <div className="flex flex-col sm:flex-row gap-4 justify-center">
                  <Link href="/tasks">
                    <button className="flex items-center gap-2 px-8 py-3 bg-white text-blue-600 rounded-md hover:bg-gray-100 hover:scale-105 transition-all text-lg font-medium">
                      Acessar Minhas Tarefas
                    </button>
                  </Link>
                  <Link href="/users">
                    <button className="flex items-center gap-2 px-8 py-3 border-2 border-white text-white rounded-md hover:bg-white/10 transition-all text-lg font-medium">
                      Gerenciar Usuários
                    </button>
                  </Link>
                </div>
              </div>
            </div>
          </section>

          {/* Features Section */}
          <section className="py-20 bg-gray-100">
            <div className="container mx-auto px-4">
              <div className="text-center mb-16">
                <h2 className="text-3xl md:text-4xl font-bold mb-4 text-gray-900">
                  Tudo que você precisa para ser mais produtivo
                </h2>
                <p className="text-lg text-gray-600 max-w-2xl mx-auto">
                  Ferramentas poderosas e intuitivas para gerenciar suas tarefas
                  e alcançar seus objetivos
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
                {features.map((feature, index) => (
                  <div
                    key={index}
                    className="bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-lg transition-all duration-300 hover:-translate-y-1 p-6"
                  >
                    <div className="mb-4">
                      <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                        <feature.icon className="w-6 h-6 text-blue-600" />
                      </div>
                      <h3 className="text-xl font-semibold text-gray-900 mb-2">
                        {feature.title}
                      </h3>
                      <p className="text-gray-600">{feature.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>

          {/* Stats Section */}
          <section className="py-20 bg-white border-y border-gray-200">
            <div className="container mx-auto px-4">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto text-center">
                <div>
                  <div className="text-4xl md:text-5xl font-bold text-blue-600 mb-2">
                    100%
                  </div>
                  <div className="text-gray-600">Controle Total</div>
                </div>
                <div>
                  <div className="text-4xl md:text-5xl font-bold text-green-600 mb-2">
                    24/7
                  </div>
                  <div className="text-gray-600">Acesso Ilimitado</div>
                </div>
                <div>
                  <div className="text-4xl md:text-5xl font-bold text-yellow-600 mb-2">
                    ∞
                  </div>
                  <div className="text-gray-600">Tarefas Ilimitadas</div>
                </div>
              </div>
            </div>
          </section>

          {/* CTA Section */}
          <section className="py-20 bg-gradient-to-br from-green-600 via-green-500 to-green-400 text-white">
            <div className="container mx-auto px-4 text-center">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">
                Pronto para aumentar sua produtividade?
              </h2>
              <p className="text-lg mb-8 opacity-95 max-w-2xl mx-auto">
                Comece agora a organizar suas tarefas e alcance seus objetivos
                com mais eficiência
              </p>
              <Link href="/tasks">
                <button className="flex items-center gap-2 px-8 py-3 bg-white text-green-600 rounded-md hover:bg-gray-100 hover:scale-105 transition-all text-lg font-medium mx-auto">
                  Começar Agora
                </button>
              </Link>
            </div>
          </section>

          {/* Footer */}
          <footer className="py-8 border-t border-gray-200 bg-white">
            <div className="container mx-auto px-4 text-center text-gray-600">
              <p>
                © 2025 Sistema de Agendamento de Tarefas. Gerencie com
                eficiência.
              </p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}

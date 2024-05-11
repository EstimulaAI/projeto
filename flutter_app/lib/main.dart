import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:textfield_tags/textfield_tags.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'EstimulaAI',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const MyHomePage(
        title: 'EstimulaAI',
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late double _distanceToField;
  late StringTagController _stringTagController;
  String _idade = "0";

  String? _selectedOption;
  final List<String> options = [
    'Andar',
    'Coordenação',
    'Relacionar',
    'Emoções',
    'Raciocínio',
    'Curiosidade',
    'Fala'
  ];
  String displayText = "";

  bool _isButtonEnabled = true;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _distanceToField = MediaQuery.of(context).size.width;
  }

  @override
  void initState() {
    super.initState();
    _stringTagController = StringTagController();
    _selectedOption = options.first;
  }

  @override
  void dispose() {
    super.dispose();
    _stringTagController.dispose();
  }

  void updateDisplayText() {
    setState(() {
      displayText = 'Tags: ${_stringTagController.getTags?.join(", ") ?? ""}\n'
          'Seleção: $_selectedOption';
    });
  }

  Future<void> generateActivity() async {
    final Uri apiUrl = Uri.parse("http://127.0.0.1:8000/");

    final Map<String, dynamic> body = {
      "idade": int.parse(_idade),
      "area": _selectedOption,
      "itens": _stringTagController.getTags ?? []
    };

    try {
      var response = await http.post(apiUrl,
          headers: {'Content-Type': 'application/json'},
          body: jsonEncode(body));

      if (response.statusCode == 201) {
        var responseBody = utf8.decode(response.bodyBytes);
        var data = jsonDecode(responseBody);

        var text = data['response'];
        setState(() {
          displayText = text;
        });
      } else {
        setState(() {
          displayText = "Erro ao buscar dados: ${response.statusCode}";
        });
      }
    } catch (e) {
      setState(() {
        displayText = "Erro ao fazer requisição: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 8.0),
        child: SingleChildScrollView(
          child: Column(
            children: [
              const SizedBox(height: 20),
              Center(
                child: Image.asset(
                  'assets/images/image.png',
                  width: 200,
                  height: 100,
                ),
              ),
              const Padding(
                padding: EdgeInsets.symmetric(horizontal: 10.0, vertical: 30.0),
                child: Text(
                  'Crie brincadeiras com qualquer coisa e estimule o desenvolvimento do seu filho! \n\nPreencha os campos abaixo e clique em GERAR para obter uma sugestão de atividade.',
                  textAlign: TextAlign.center,
                ),
              ),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 10.0),
                child: TextField(
                  controller: TextEditingController(text: _idade),
                  decoration: const InputDecoration(
                    labelText: 'Idade da criança',
                    contentPadding:
                        EdgeInsets.symmetric(horizontal: 10.0, vertical: 10.0),
                    border: OutlineInputBorder(
                        borderSide: BorderSide(color: Colors.lightBlue)),
                  ),
                  keyboardType: TextInputType.number,
                  inputFormatters: [FilteringTextInputFormatter.digitsOnly],
                  onChanged: (String value) {
                    setState(() {
                      _idade = value;
                    });
                  },
                ),
              ),
              const SizedBox(height: 20),
              TextFieldTags<String>(
                textfieldTagsController: _stringTagController,
                textSeparators: const [','],
                letterCase: LetterCase.normal,
                validator: (String tag) {
                  if (tag == 'faca') {
                    return 'Não é um objeto permitido.';
                  } else if (_stringTagController.getTags!.contains(tag)) {
                    return 'Você já adicionou esse objeto.';
                  }
                  return null;
                },
                inputFieldBuilder: (context, inputFieldValues) {
                  return Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 10.0),
                    child: TextField(
                      onTap: () {
                        _stringTagController.getFocusNode?.requestFocus();
                      },
                      controller: inputFieldValues.textEditingController,
                      focusNode: inputFieldValues.focusNode,
                      decoration: InputDecoration(
                        isDense: true,
                        border: const OutlineInputBorder(
                          borderSide: BorderSide(
                            // cyan
                            color: Colors.lightBlue,
                            width: 3.0,
                          ),
                        ),
                        focusedBorder: const OutlineInputBorder(
                          borderSide: BorderSide(
                            color: Colors.lightBlue,
                            width: 3.0,
                          ),
                        ),
                        helperStyle: const TextStyle(
                          color: Colors.lightBlue,
                        ),
                        hintText: inputFieldValues.tags.isNotEmpty
                            ? ''
                            : "Objetos...",
                        errorText: inputFieldValues.error,
                        prefixIconConstraints:
                            BoxConstraints(maxWidth: _distanceToField * 0.8),
                        prefixIcon: inputFieldValues.tags.isNotEmpty
                            ? SingleChildScrollView(
                                controller:
                                    inputFieldValues.tagScrollController,
                                scrollDirection: Axis.vertical,
                                child: Padding(
                                  padding: const EdgeInsets.only(
                                    top: 8,
                                    bottom: 8,
                                    left: 8,
                                  ),
                                  child: Wrap(
                                      runSpacing: 4.0,
                                      spacing: 4.0,
                                      children: inputFieldValues.tags
                                          .map((String tag) {
                                        return Container(
                                          decoration: const BoxDecoration(
                                            borderRadius: BorderRadius.all(
                                              Radius.circular(20.0),
                                            ),
                                            color: Colors.lightBlue,
                                          ),
                                          margin: const EdgeInsets.symmetric(
                                              horizontal: 5.0),
                                          padding: const EdgeInsets.symmetric(
                                              horizontal: 10.0, vertical: 5.0),
                                          child: Row(
                                            mainAxisAlignment:
                                                MainAxisAlignment.start,
                                            mainAxisSize: MainAxisSize.min,
                                            children: [
                                              InkWell(
                                                child: Text(
                                                  tag,
                                                  style: const TextStyle(
                                                      color: Colors.white),
                                                ),
                                                onTap: () {
                                                  //print("$tag selected");
                                                },
                                              ),
                                              const SizedBox(width: 4.0),
                                              InkWell(
                                                child: const Icon(
                                                  Icons.cancel,
                                                  size: 14.0,
                                                  color: Color.fromARGB(
                                                      255, 233, 233, 233),
                                                ),
                                                onTap: () {
                                                  inputFieldValues
                                                      .onTagRemoved(tag);
                                                },
                                              )
                                            ],
                                          ),
                                        );
                                      }).toList()),
                                ),
                              )
                            : null,
                      ),
                      onChanged: inputFieldValues.onTagChanged,
                      onSubmitted: inputFieldValues.onTagSubmitted,
                    ),
                  );
                },
              ),
              const SizedBox(height: 20),
              DropdownMenu<String>(
                label: const Text('Quero estimular:'),
                initialSelection: _selectedOption,
                onSelected: (String? newValue) {
                  setState(() {
                    _selectedOption = newValue!;
                  });
                },
                expandedInsets: const EdgeInsets.symmetric(
                  horizontal: 10.0,
                  vertical: 10.0,
                ),
                dropdownMenuEntries:
                    options.map<DropdownMenuEntry<String>>((String value) {
                  return DropdownMenuEntry<String>(value: value, label: value);
                }).toList(),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.resolveWith<Color>(
                    (Set<MaterialState> states) {
                      if (states.contains(MaterialState.disabled)) {
                        return Colors.grey;
                      }
                      return Colors.lightBlue;
                    },
                  ),
                  foregroundColor: MaterialStateProperty.resolveWith<Color>(
                    (Set<MaterialState> states) {
                      if (states.contains(MaterialState.disabled)) {
                        return Colors.white;
                      }
                      return Colors.white;
                    },
                  ),
                ),
                onPressed: _isButtonEnabled
                    ? () {
                        setState(() {
                          _isButtonEnabled = false; // Desabilita o botão
                        });
                        generateActivity().then((_) {
                          setState(() {
                            _isButtonEnabled =
                                true; // Reabilita o botão após a função assíncrona
                          });
                        });
                      }
                    : null, // Funcionalidade do botão desabilitada baseada no estado
                child: const Text(
                  'GERAR',
                  style: TextStyle(color: Colors.white),
                ),
              ),
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.all(20.0),
                child: Text(
                  displayText,
                  textAlign: TextAlign.center,
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
